# Daily Question: 2025-02-13
# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii

import heapq
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums = [x for x in nums if x < k]
        heapq.heapify(nums)
        sol = 0

        while len(nums) >= 1:
            sol += 1
            if len(nums) == 1:
                break
            x, y = heapq.heappop(nums), heapq.heappop(nums)

            z = 2 * x + y
            if z < k:
                heapq.heappush(nums, z)

        return sol


# Time: O(nlogn) where n is the length of nums
# Space: O(n)
