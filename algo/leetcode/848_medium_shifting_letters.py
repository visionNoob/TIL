# @2025-01-05
# https://leetcode.com/problems/shifting-letters/

from itertools import accumulate
from types import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:

        return "".join(
            chr(97 + (ord(ch) - 97 + shift) % 26)
            for ch, shift in zip(s, list(accumulate(shifts[::-1]))[::-1])
        )


# Time: O(n) where n is the length of the string
# Space: O(n)
