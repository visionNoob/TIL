# Daily Question: 2025-03-31
# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values


from types import List
from typing import Tuple


# Method1: Two Pointers
class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:

        p1, p2 = 0, 0
        sol = []
        while p1 < len(nums1) or p2 < len(nums2):
            id1, id2 = (
                nums1[min(p1, len(nums1) - 1)][0],
                nums2[min(p2, len(nums2) - 1)][0],
            )

            if p1 >= len(nums1):
                sol.append(nums2[p2])
                p2 += 1
            elif p2 >= len(nums2):
                sol.append(nums1[p1])
                p1 += 1
            elif id1 > id2:
                sol.append(nums2[p2])
                p2 += 1
            elif id1 < id2:
                sol.append(nums1[p1])
                p1 += 1
            else:
                sol.append([nums1[p1][0], nums1[p1][1] + nums2[p2][1]])
                p1 += 1
                p2 += 1

        return sol
