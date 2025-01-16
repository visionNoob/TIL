# Daily Question: 2025-01-16
# https://leetcode.com/problems/bitwise-xor-of-all-pairings

from typing import List


class Solution:

    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:

        sol = 0
        if len(nums1) & 1:
            for n in nums2:
                sol ^= n
        if len(nums2) & 1:
            for n in nums1:
                sol ^= n
        return sol


# Time: O(n)
# Space: O(1)
# inpired by https://leetcode.com/problems/bitwise-xor-of-all-pairings/solutions/2646552/java-c-python-easy-and-concise/
