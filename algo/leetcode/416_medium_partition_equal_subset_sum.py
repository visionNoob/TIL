# leetcode 416. Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum
# inpired by https://leetcode.com/problems/partition-equal-subset-sum/description/


from typing import List

# Method 1: Brute Force


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target_sum = sum(nums)
        if target_sum % 2:
            return False
        target_sum = target_sum // 2

        l = [0]
        for n in nums:
            sz = len(l)
            for i in range(sz):
                l.append(l[i] + n)

        return any(x == target_sum for x in l)


# Memory Limit Exceeded
# Time: O(2^n)
# Space: O(2^n)

# Method 2: Backtracking with recursion


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2:
            return False

        target = target // 2

        def backtracking(current_sum, idx):
            if current_sum > target or idx >= len(nums):
                return False

            if current_sum == target:
                return True

            return backtracking(current_sum + nums[idx], idx + 1) or backtracking(
                current_sum, idx + 1
            )

        return backtracking(0, 0)


# Memory Limit Exceeded
# Time: O(2^n)
# Space: O(n)
