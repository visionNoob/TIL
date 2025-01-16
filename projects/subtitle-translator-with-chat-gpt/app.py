import os
import sys
import gradio as gr
import dotenv

sys.path.append(".")  # Adds the module to path

import translator
import shared
import utils


dotenv.load_dotenv()


def update_api_key(api_key):

    client = utils.init_client(api_key)

    if not client:
        raise ValueError("❌ Invalid API Key.  Please check and try again. 🔄")
    else:
        shared.client = client
        shared.models = [x.id for x in client.models.list() if "gpt-4o" in x.id]
        dropdown_update = gr.Dropdown(
            choices=shared.models,
            value="gpt-4o",
        )
        return (f"✅ API Key is successfully set! 🎉"), dropdown_update


def upload_file(file):
    """
    Reads an .srt file and returns its contents as text.
    """
    if not file.endswith(".srt"):
        return "❌ Invalid file format. Please upload an .srt file."

    try:
        with open(file, "r", encoding="utf-8") as f:
            shared.save_dir = os.path.dirname(file)
            shared.basename = os.path.basename(file).replace(".srt", "_kor.srt")

            contents = f.read()

        with open(file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        return contents, lines
    except Exception as e:
        return f"⚠️ Error reading file: {e}"


def translate_subtitles(
    subtitles, model, system_prompt, user_prompt, progress=gr.Progress()
):
    """
    Translates the subtitles using the OpenAI API.
    """
    if not subtitles:
        return "❌ Please upload a valid .srt file."

    sub_translator = translator.Translator(shared.client, subtitles)

    progress(0, desc="Starting...")
    translated_subtitles = sub_translator.translate(
        model, system_prompt, user_prompt, progress
    )

    save_dir = os.path.join(shared.save_dir, shared.basename)
    with open(save_dir, "w", encoding="utf-8") as f:
        f.write(translated_subtitles)

    return translated_subtitles, save_dir


with gr.Blocks() as demo:

    gr.Markdown("# 1️⃣ Activate OpenAI API Key")
    openapi_key = gr.Textbox(
        value=os.getenv("OPENAI_API_KEY"),
        placeholder="Enter your OpenAI API Key",
        label="API Key",
        lines=2,
    )

    save_button = gr.Button("Activate", variant="secondary")

    status_markdown = gr.Markdown("Please enter your OpenAI API Key.")

    gr.Markdown("# 2️⃣ Configuration")
    dropdown_models = gr.Dropdown(label="Model", interactive=True)
    with gr.Accordion("Prompt", open=True):
        system_prompt = gr.Textbox(
            show_copy_button=True,
            label="System Prompt",
            lines=5,
            value=shared.system_prompt,
            interactive=True,
        )
        user_prompt = gr.Textbox(
            show_copy_button=True,
            label="User Prompt",
            lines=5,
            value=shared.user_prompt,
            interactive=True,
        )

    gr.Markdown("# 3️⃣ Upload Subtitles")
    file_output = gr.File(
        label="Upload Subtitles", type="filepath", file_types=[".srt"]
    )

    lines = gr.State()
    with gr.Row():
        with gr.Column():
            gr.Markdown("# 4️⃣ Original Subtitles")
            text_box = gr.Textbox(show_copy_button=True, label="Input Subtitles")
            button_translate = gr.Button("Translate", variant="stop")
        with gr.Column():
            gr.Markdown("# 5️⃣ Translated Subtitles")
            text_output = gr.Textbox(
                show_copy_button=True, label="Translated Subtitles"
            )
            button_download = gr.DownloadButton("Download", variant="secondary")

    file_output.upload(upload_file, file_output, [text_box, lines])

    save_button.click(
        fn=update_api_key,
        inputs=openapi_key,
        outputs=[status_markdown, dropdown_models],
    )

    button_translate.click(
        translate_subtitles,
        [lines, dropdown_models, system_prompt, user_prompt],
        [text_output, button_download],
    )

demo.launch()
