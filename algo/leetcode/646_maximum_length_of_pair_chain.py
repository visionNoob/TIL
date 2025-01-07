# @2025-01-07
# https://leetcode.com/problems/maximum-length-of-pair-chain

from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        sol, pos = 0, -1001

        for s, e in pairs:
            if pos < s:
                sol += 1
                pos = e
                continue

        return sol


# Time: O(nlogn)
# Space: O(1)
