# Daily Question: 2015-01-22
# https://leetcode.com/problems/map-of-highest-peak

from typing import List
from collections import deque

DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:

        # O(1)
        height, width = len(isWater), len(isWater[0])

        # O(m * n) where m is the height and n is the width
        sol = [[-1] * width for _ in range(height)]

        # O(m * n)
        queue = deque(
            [(j, i) for j in range(height) for i in range(width) if isWater[j][i]]
        )

        # O(m * n)
        for j, i in queue:
            sol[j][i] = 0

        # O(m * n)
        while queue:
            j, i = queue.popleft()

            for dj, ji in DIRECTIONS:
                nj, ni = j + dj, i + ji

                if 0 <= nj < height and 0 <= ni < width and sol[nj][ni] == -1:
                    sol[nj][ni] = sol[j][i] + 1
                    queue.append((nj, ni))
        return sol


# Time: O(m * n)
# Space: O(m * n)
