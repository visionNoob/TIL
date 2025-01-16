import os
import sys
import json
import openai
from openai import OpenAI
import re
from dotenv import load_dotenv
from typing import List, Generator
import tqdm
import logging
import shared
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Translator:
    def __init__(self, client: OpenAI, lines: List[str]):
        self.client = client
        self.lines = lines
        self.subtitles = self.split_srt_into_subtitles(lines)
        pass

    def translate_subtitle_block(
        self,
        block: List[str],
        model: str,
        system_prompt: str,
        user_prompt: str,
    ) -> List[str]:
        """
        Translates a single subtitle block using the OpenAI API, while preserving
        sequence numbers, time ranges, and empty lines.
        """

        translated_block = []
        dialogue_lines = []

        # 1) Separate dialogue lines from sequence/time info
        for line in block:
            if re.match(r"^\d+$", line.strip()):
                # Subtitle sequence number
                translated_block.append(line)
            elif re.match(
                r"^\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}", line.strip()
            ):
                # Time range
                translated_block.append(line)
            elif line.strip() == "":
                # Empty lines
                translated_block.append(line)
            else:
                # Actual dialogue
                dialogue_lines.append(line.strip())

        # 2) Translate dialogue if present
        if dialogue_lines:
            to_translate_text = "\n".join(dialogue_lines)
            response = self.create_chat_completion_request(
                model=model,
                system_prompt=system_prompt,
                user_prompt=user_prompt,
                text=to_translate_text,
            )
            translated_text = response.choices[0].message.content.strip()

            # Split the translated text back into lines
            translated_lines = translated_text.split("\n")

            # Adjust the number of translated lines to match the original dialogue line count
            if len(translated_lines) < len(dialogue_lines):
                translated_lines += [""] * (len(dialogue_lines) - len(translated_lines))
            elif len(translated_lines) > len(dialogue_lines):
                translated_lines = translated_lines[: len(dialogue_lines)]

            # 3) Append the translated dialogue
            for line_t in translated_lines:
                translated_block.append(line_t + "\n")

        return translated_block

    def create_chat_completion_request(
        self, model: str, system_prompt: str, user_prompt: str, text: str
    ):
        """
        Example of combining system/user prompts with context (both English + previously translated Korean).
        """
        # system_prompt 에 extra_instruction 을 덧붙인다.
        system_content = system_prompt + "\n\n"  # 구분용 공백

        messages = [
            {"role": "system", "content": system_content},
            {
                "role": "user",
                "content": (
                    f"{user_prompt}\n\n" f"--- Target to Translate ---\n{text}"
                ),
            },
        ]

        return self.client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.2,
        )

    def merge_subtitles(self, subtitles: List[List[str]]) -> List[str]:
        """
        Merges a list of subtitle blocks back into a single list of SRT lines.

        Args:
            subtitles (List[List[str]]): List of subtitle blocks.

        Returns:
            List[str]: Merged list of all SRT lines.
        """
        merged_lines = []
        for sub in subtitles:
            merged_lines.extend(sub)
            merged_lines.append("\n")

        # merge to single string
        merged_lines = "".join(merged_lines)
        return merged_lines

    def translate(
        self, model: str, system_prompt: str, user_prompt: str, progress=tqdm
    ):

        translated_blocks: List[List[str]] = [[] for _ in range(len(self.subtitles))]

        for i in progress.tqdm(
            range(len(self.subtitles)), desc="Translating with Sliding Window"
        ):
            new_translated_block = self.translate_subtitle_block(
                block=self.subtitles[i],
                model=model,
                system_prompt=system_prompt,
                user_prompt=user_prompt,
            )

            translated_blocks[i] = new_translated_block

        return self.merge_subtitles(translated_blocks)

    def split_srt_into_subtitles(self, lines: List[str]) -> List[List[str]]:
        """
        Splits a list of SRT lines into subtitle blocks.

        Each block typically contains:
        - A sequence number (e.g., "1")
        - A time range (e.g., "00:00:00,000 --> 00:00:05,000")
        - One or more lines of dialogue
        - A blank line (separator)

        Args:
            lines (List[str]): The entire SRT file lines.

        Returns:
            List[List[str]]: A list of subtitle blocks, where each block is itself a list of lines.
        """
        subtitles = []
        current_sub = []

        for line in lines:
            if line.strip() == "" and current_sub:
                subtitles.append(current_sub)
                current_sub = []
            else:
                current_sub.append(line)

        # Handle the last block if it exists
        if current_sub:
            subtitles.append(current_sub)

        return subtitles
