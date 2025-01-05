# @2025-01-05
# https://leetcode.com/problems/maximum-population-year/

from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        populations = [0] * 100

        for b, d in logs:  # O(n)
            for i in range(b - 1950, d - 1950):  # O(100) = O(1)
                populations[i] += 1

        sol = 0
        max_p = 0
        for i, p in enumerate(populations):  # O(100) = O(1)
            if max_p < p:
                max_p = p
                sol = i

        return sol + 1950


# Time: O(n) where n is the length of the logs
# Space: O(1)
