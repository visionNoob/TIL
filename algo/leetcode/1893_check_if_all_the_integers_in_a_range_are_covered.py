# @2025-07-07
# https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered

from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        table = [0] * 50

        for s, e in ranges:
            table[s - 1 : e] = [True] * (e - s + 1)

        return all(table[left - 1 : right])


# Time: O(n)
# Space: O(1)
