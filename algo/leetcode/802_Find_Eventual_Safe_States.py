# Daily Question: 2015-01-24
# https://leetcode.com/problems/find-eventual-safe-states/description/?envType=daily-question&envId=2025-01-24


from typing import List


# Method 1: its my first attempt.
class Solution:

    def is_safe(self, graph, idx, goods, bads, visit):

        if idx in visit:
            return False

        visit.add(idx)

        for node in graph[idx]:
            if node == idx:
                bads.add(node)
                return False

            if not node in bads and (
                node in goods or self.is_safe(graph, node, goods, bads, visit.copy())
            ):
                goods.add(node)
                continue

            bads.add(node)
            return False

        return True

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        goods, bads = set(), set()

        return [
            idx
            for idx in range(len(graph))
            if not idx in bads
            and (idx in goods or self.is_safe(graph, idx, goods, bads, set()))
        ]


# Time: O(n + m) where n is the length of graph and m is the length of the longest path in the graph
# Space: O(n)
