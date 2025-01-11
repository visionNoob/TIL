# Daily Question: 2025-01-07
# https://leetcode.com/problems/string-matching-in-an-array

from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        merged = " ".join(words)
        return [x for x in words if merged.count(x) > 1]


# Time: O(n^2)
# Space: O(n)
