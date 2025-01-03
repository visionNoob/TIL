# @2025-01-03
# https://leetcode.com/problems/balanced-binary-tree

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_depth(self, node):
        if not node:
            return True, 0

        is_lb, l_depth = self.get_depth(node.left)
        is_rb, r_depth = self.get_depth(node.right)

        is_balanced = is_lb & is_rb & (abs(l_depth - r_depth) < 2)

        return is_balanced, max(l_depth + 1, r_depth + 1)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced, _ = self.get_depth(root)
        return is_balanced


# Time: O(n) where n is the number of nodes in the tree
# Space: O(n)
