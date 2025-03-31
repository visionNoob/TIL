# Daily Question: 2025-03-31
# https://leetcode.com/problems/apply-operations-to-an-array

from types import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        sol = []

        for i in range(len(nums)):
            if i + 1 != len(nums) and nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            if nums[i] != 0:
                sol.append(nums[i])

        return sol + [0] * (len(nums) - len(sol))


# Time: O(N) where N is the length of the nums array
# Space: O(N) for the sol array
