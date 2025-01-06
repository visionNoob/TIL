# Daily Question: 2025-01-05
# https://leetcode.com/problems/shifting-letters-ii

from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        deltas = [0] * (len(s) + 1)

        for start, end, d in shifts:
            d = -1 if d == 0 else 1
            deltas[start] += d
            deltas[end + 1] += d * -1

        prefix, sol = 0, ""
        for d, c in zip(deltas, s):
            prefix += d
            sol += chr(97 + (ord(c) - 97 + prefix) % 26)
        return sol


# Time: O(n) where n is the length of the string
# Space: O(n)
