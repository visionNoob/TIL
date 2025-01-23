# Daily Qeustion: 2015-01-23
# https://leetcode.com/problems/count-servers-that-communicate

from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        connected_servers = 0

        for j in range(rows):
            num_servers = sum(grid[j])
            connected_servers += num_servers
            if num_servers == 1:
                for i in range(cols):
                    if grid[j][i] == 1:
                        connected_servers -= sum(grid[x][i] for x in range(rows)) == 1
                        break

        return connected_servers


# Time: O(m * n) where m is the number of rows and n is the number of columns
# Space: O(1)
