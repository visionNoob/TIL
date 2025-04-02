# Daily Question: 2025-04-01
# https://leetcode.com/problems/solving-questions-with-brainpower/
from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        max_point = 0
        dp = [0] * len(questions)

        for i in range(len(questions) - 1, -1, -1):
            point, brainpower = questions[i]
            if i + brainpower + 1 < len(questions):
                point += dp[i + brainpower + 1]
            dp[i] = max_point = max(max_point, point)

        return max_point


# Time Complexity: O(n)
# Space Complexity: O(n)
