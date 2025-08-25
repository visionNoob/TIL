# leetcode 498. Diagonal Traverse
# https://leetcode.com/problems/diagonal-traverse/?envType=daily-question&envId=2025-08-25


from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diags = []
        height, width = len(mat), len(mat[0])
        j, i, up = 0, 0, True

        for _ in range(height * width):
            # print(j, i)
            diags.append(mat[j][i])
            
            if up:
                if i == width - 1:
                    j += 1
                    up = False
                elif j == 0:
                    i += 1
                    up = False
                else:
                    j -= 1
                    i += 1
            else:
                if j == height - 1:
                    i += 1
                    up = True
                elif i == 0:
                    j += 1
                    up = True
                else:
                    j += 1
                    i -= 1
        
        return diags


# Time: O(m * n)
# Space: O(1)