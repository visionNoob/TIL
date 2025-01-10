# Daily Question: 2015-01-10
# https://leetcode.com/problems/word-subsets
# Sol is inpired by https://leetcode.com/problems/word-subsets/solutions/2353565/solution-using-counter-in-python/?envType=daily-question&envId=2025-01-10
# But I didn't use Counter, I used defaultdict(int) instead.

from typing import List
from collections import defaultdict


class Solution:

    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        words2 = list(set(words2))

        table2 = defaultdict(int)
        for word2 in words2:
            tmp = defaultdict(int)
            for c in word2:
                tmp[c] = tmp[c] + 1

            for k, v in tmp.items():
                table2[k] = max(table2[k], v)

        sol = []
        for word1 in words1:
            table1 = defaultdict(int)
            for c in word1:
                table1[c] = table1[c] + 1

            universal = True
            for k, v in table2.items():
                if not k in table1 or table1[k] < v:
                    universal = False
            if universal:
                sol.append(word1)

        return sol


# Time: O(n + m) where n is the length of words1 and m is the length of words2
# Space: O(n + m)
