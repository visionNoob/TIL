# Daily Question: 2025-01-06
# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box

from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        indices = [i + 1 for i in range(len(boxes)) if boxes[i] == "1"]

        l, c, r, ops = 0, 0, len(indices), sum(indices)

        sol = []

        for box in boxes:
            l += c
            c = 0 if box == "0" else 1
            r -= c
            ops = ops - c - r + l
            sol.append(ops)
        return sol


# Time: O(n) where n is the length of boxes
# Space: O(n)
