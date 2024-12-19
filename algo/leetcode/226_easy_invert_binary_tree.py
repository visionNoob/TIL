# Top Interview 150 : 2024-12-19
# https://leetcode.com/problems/invert-binary-tree

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            stack.extend(filter(None, (node.left, node.right)))

        return root


# Time: O(n)
# Space: O(n)
