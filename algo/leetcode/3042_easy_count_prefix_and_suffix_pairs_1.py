# Daily Question: 2025-01-08
# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i

from itertools import combinations
from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        sol = 0
        for s1, s2 in combinations(words, 2):
            if s2.startswith(s1) and s2.endswith(s1):
                sol += 1
        return sol


# Time: O(n^2)
# Space: O(1)
