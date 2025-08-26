# leetcode 3000. Maximum Area of Longest Diagonal Rectangle
# https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle


from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        
        max_area = 0
        max_diagonal = 0

        for w, h in dimensions:
            diagonal = w * w + h * h
            if diagonal > max_diagonal:
                max_area = w * h
                max_diagonal = diagonal
            elif diagonal == max_diagonal:
                max_area = max(max_area, w * h)
                
        
        return max_area


# Find rectangle with longest diagonal, return max area if tie
# Time: O(n)
# Space: O(1)