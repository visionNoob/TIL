# Daily Question: 2025-03-28
# https://leetcode.com/problems/maximum-number-of-points-from-grid-queries

from queue import PriorityQueue
from types import List
from typing import Tuple


# Approach1: BFS + Priority Queue
# Time: O(N * M * log(N * M)) where N is the height of the grid and M is the width of the grid
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        height, width, ans = len(grid), len(grid[0]), [0] * len(queries)
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        queries = sorted([(q, idx) for idx, q in enumerate(queries)])  #

        min_heap = PriorityQueue()
        visited = [[False] * width for _ in range(height)]

        visited[0][0] = True
        min_heap.put((grid[0][0], 0, 0))
        point = 0
        for query, q_idx in queries:
            while not min_heap.empty() and min_heap.queue[0][0] < query:
                c_val, y, x = min_heap.get()
                point += 1

                for offset_y, offset_x in DIRS:
                    new_y = y + offset_y
                    new_x = x + offset_x

                    if (
                        width > new_x >= 0
                        and height > new_y >= 0
                        and not visited[new_y][new_x]
                    ):
                        visited[new_y][new_x] = True
                        min_heap.put((grid[new_y][new_x], new_y, new_x))

            ans[q_idx] = point

        return ans
