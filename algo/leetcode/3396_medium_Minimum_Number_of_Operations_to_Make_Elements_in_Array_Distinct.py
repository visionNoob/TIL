# Daily Question: 2025-04-08
# https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/

from typing import List
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen, state = set(), False
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in seen:
                state = True
                break
            seen.add(nums[i])

        return (i + 3) // 3 if state else 0

# Time Complexity: O(n)
# Space Complexity: O(n)