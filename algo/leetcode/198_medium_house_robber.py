# Job Interview 150 : 2025-01-08
# https://leetcode.com/problems/house-robber

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [nums[0], max(nums[:2])]

        for i in range(2, n):
            dp.append(max(dp[i - 2] + nums[i], dp[i - 1]))
        return dp[-1]


# Time: O(n) where n is the length of nums
# Space: O(n)
