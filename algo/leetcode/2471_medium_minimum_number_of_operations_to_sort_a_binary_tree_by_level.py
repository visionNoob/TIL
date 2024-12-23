# Daily Question: 2024-12.23
# https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:

        ans = 0
        queue = deque([root])

        while queue:

            vals = sorted([(queue[i].val, i) for i in range(len(queue))])
            indices = [x[1] for x in vals]

            for i in range(len(indices)):
                j = indices[i]
                while i != j:
                    indices[i], indices[j] = indices[j], indices[i]
                    j = indices[i]
                    ans += 1

            for _ in range(len(queue)):
                node = queue.popleft()
                queue.extend(filter(None, (node.left, node.right)))

        return ans


# Time: O(n*log(n))
# Space: O(n)
