# Daily Question: 2025-01-09
# https://leetcode.com/problems/counting-words-with-a-given-prefix/

from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        sol = 0
        for word in words:
            if word.startswith(pref):
                sol += 1
        return sol


# Time: O(n * m) where n is the length of words and m is the length of pref
# Space: O(1)
