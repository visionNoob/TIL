# Daily Question: 2025-01-20
# https://leetcode.com/problems/first-completely-painted-row-or-column


from typing import List


# Method 1: My Solution
class Solution:

    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])

        if rows == 1 or cols == 1:
            return 0

        table = {mat[j][i]: (j, i) for j in range(rows) for i in range(cols)}

        row_table = {x: cols for x in range(rows)}
        col_table = {x: rows for x in range(cols)}
        # feedback: table을 그냥 zero-initialize 로 선언하고 더해주는게 더 빠름

        for idx, num in enumerate(arr):

            j, i = table[num]
            row_table[j] -= 1
            col_table[i] -= 1

            if row_table[j] == 0 or col_table[i] == 0:
                return idx

        assert False


# Method 2: Without using dictionary
# This is the better solution because it doesn't use dictionary.
# A dictionary is bad when the keys are integers from 0 to n-1.
# that has a lot of memory overhead.
class Solution:

    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])

        if rows == 1 or cols == 1:
            return 0

        table = [-1] * len(arr)

        for j in range(rows):
            for i in range(cols):
                val = mat[j][i]
                table[val - 1] = (j, i)

        row_table = [0] * rows
        col_table = [0] * cols

        for idx, num in enumerate(arr):

            j, i = table[num - 1]
            row_table[j] += 1
            col_table[i] += 1

            if row_table[j] == cols or col_table[i] == rows:
                return idx

        assert False


# Time: O(n) where n is the number of elements in the matrix
# Space: O(n)
