# Daily Question: 2025-01-03
# https://leetcode.com/problems/number-of-ways-to-split-array

from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        valid_splits = 0
        left_sum = 0
        target = sum(nums) / 2

        for num in nums[:-1]:
            left_sum += num
            valid_splits += target <= left_sum

        return valid_splits


# Time: O(n) where n is the lenght of nums
# Space: O(1)
