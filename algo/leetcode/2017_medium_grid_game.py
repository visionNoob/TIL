# Daily Question: 2015-01-21
# https://leetcode.com/problems/grid-game/submissions/1518593036/?envType=daily-question&envId=2025-01-21

from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:

        top_score, bottom_score, optimal_score = sum(grid[0]), 0, float("inf")

        for i in range(len(grid[0])):
            top_score -= grid[0][i]
            optimal_score = min(optimal_score, max(top_score, bottom_score))
            bottom_score += grid[1][i]

        return optimal_score


# Time: O(n) where n is the length of grid
# Space: O(1)
