# Daily Question: 2025-01-17
# https://leetcode.com/problems/neighboring-bitwise-xor

from typing import List


# Method 1
# if the number of 1s in the array is even, then the last element should be 0
# if the number of 1s in the array is odd, then the last element should be 1
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        if len(derived) == 1:
            return derived[0] == 0

        return derived[:-1].count(1) % 2 == derived[-1]


# Method 2
# But Method1 means we need to count the number of 1s in the array, which is not necessary
# We can just check if the number of 1s in the array is even or not
# I was pool in the first method, but I think this is the best solution
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:

        return not derived.count(1) & 1


#  Time: O(n)
#  Space: O(1)
