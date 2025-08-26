# leetcode 119. Pascal's Triangle II
# https://leetcode.com/problems/pascals-triangle-ii


from typing import List
from functools import lru_cache


# Method 1: Naive Approach with manual cache
# class Solution:
#     def getRow(self, rowIndex: int) -> List[int]:
#         sol = []
#         cache = dict()

#         def foo(row, idx):
#             if idx < 0 or idx > row:
#                 return 0
#             if row == 0:
#                 return 1

#             if idx - 1 < 0 or idx - 1 > row:
#                 v1 = 0
#             elif (row - 1, idx - 1) in cache:
#                 v1 = cache.get((row - 1, idx - 1))
#             else:
#                 v1 = foo(row - 1, idx - 1)
#                 cache[(row - 1, idx - 1)] = v1

#             if idx < 0 or idx > row:
#                 v2 = 0
#             elif (row - 1, idx) in cache:
#                 v2 = cache.get((row - 1, idx))
#             else:
#                 v2 = foo(row - 1, idx)
#                 cache[(row - 1, idx)] = v2

#             return v1 + v2

#         for i in range(rowIndex + 1):
#             sol.append(foo(rowIndex, i))
#         return sol

# Manual memoization with recursive approach
# Time: O(rowIndex^2)
# Space: O(rowIndex^2)


# Method 2: lru_cache with elegant border handling
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        @lru_cache(None)
        def C(n, k):
            if k == 0 or k == n:
                return 1
            return C(n-1, k-1) + C(n-1, k)

        return [C(rowIndex, k) for k in range(rowIndex + 1)]

# Combination formula C(n,k) with built-in memoization
# Time: O(rowIndex^2)
# Space: O(rowIndex^2)