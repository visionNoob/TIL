# Top Interview 150: 2024-12-23
# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        table = defaultdict(list)
        for s in strs:
            sorted_string = "".join(sorted(s))
            table[sorted_string].append(s)

        return list(table.values())


# Time: O(n*m*log(m))
# Space: O(n*m)
# where n is the number of strings and m is the length of the longest string
