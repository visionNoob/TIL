# Top Interview 150 : 2024-12-20
# https://leetcode.com/problems/set-matrix-zeroes/
# Duration: 04:25

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        height = len(matrix)
        width = len(matrix[0])

        lookup_h = [False] * height
        lookup_w = [False] * width

        for j in range(height):
            for i in range(width):
                if matrix[j][i] == 0:
                    lookup_h[j] = matrix[j][i] == 0
                    lookup_w[i] = matrix[j][i] == 0

        for j in range(height):
            for i in range(width):
                if lookup_h[j] or lookup_w[i]:
                    matrix[j][i] = 0


# Time: O(n*m)
# Space: O(n+m)
