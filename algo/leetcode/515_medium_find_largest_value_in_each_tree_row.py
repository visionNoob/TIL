# Daily Question: 2024-12-25
# https://leetcode.com/problems/find-largest-value-in-each-tree-row

# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        sol = []
        queue = deque([root])

        while queue:
            sz = len(queue)

            for i in range(sz):
                max_val = queue[i].val if i == 0 else max(max_val, queue[i].val)
            sol.append(max_val)

            for _ in range(sz):
                node = queue.popleft()
                queue.extend(filter(None, (node.left, node.right)))

        return sol


# Time: O(n)
# Space: O(n)
