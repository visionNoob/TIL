# Daily Question: 2025-01-02
# https://leetcode.com/problems/count-vowel-strings-in-ranges

from itertools import accumulate
from typing import List


# Method 1: Prefix Sum (Fastest)
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a", "e", "i", "o", "u"}
        prefix_sum = [0]

        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                prefix_sum.append((prefix_sum[i] + 1))
            else:
                prefix_sum.append((prefix_sum[i]))

        return [prefix_sum[e + 1] - prefix_sum[s] for s, e in queries]


# Method 2: Prefix Sum (Concise but slower)
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a", "e", "i", "o", "u"}
        vowel_bools = [1 if w[0] in vowels and w[-1] in vowels else 0 for w in words]
        prefix_sum = [0] + list(accumulate(vowel_bools))

        return [prefix_sum[e + 1] - prefix_sum[s] for s, e in queries]


# Time: O(n) where n is the length of words
# Space: O(n)
