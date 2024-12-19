# Daily Question @ 2024-12-19
# https://leetcode.com/problems/max-chunks-to-make-sorted

from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_num = chunks = carries = 0

        for idx, num in enumerate(arr):
            max_num = max(max_num, num)
            if max_num > idx:
                continue

            if max_num > idx:
                chunks += carries
                carries = 0
            else:
                carries += 1

        return chunks + carries


# Time: O(n)
# Space: O(1)
