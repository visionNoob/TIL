# Daily Question: 2024-12-24
# https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs

from collections import defaultdict, deque
from typing import List


class Solution:
    def diameter(self, edges):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(start):
            visited = set()
            queue = deque([(start, 0)])  # (node, distance)
            visited.add(start)
            fartest_node, max_dist = start, 0

            while queue:
                node, dist = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, dist + 1))

                        if dist + 1 > max_dist:
                            max_dist = dist + 1
                            fartest_node = neighbor
            return fartest_node, max_dist

        node_a, _ = bfs(0)
        _, diameter = bfs(node_a)
        return diameter

    def minimumDiameterAfterMerge(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> int:
        d1 = self.diameter(edges1)
        d2 = self.diameter(edges2)
        return max(d1, d2, (d1 + 1) // 2 + (d2 + 1) // 2 + 1)


# Time: O(n + m)
# Space: O(n + m)
