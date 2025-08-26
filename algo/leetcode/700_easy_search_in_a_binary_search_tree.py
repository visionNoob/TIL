# leetcode 700. Search in a Binary Search Tree
# https://leetcode.com/problems/search-in-a-binary-search-tree


from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Method 1: Iterative Version 
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        node = root
        while True:
            if node.val == val:
                return node
            
            elif val < node.val:
                if not node.left:
                    return None
                node = node.left
            elif val > node.val:
                if not node.right:
                    return None
                node = node.right
                pass
            else:
                assert False

        assert False

# Binary search with while loop
# Time: O(log n)
# Space: O(1)


# Method 2: Recursive Version
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return None
        elif val == root.val: return root
        elif val < root.val: return self.searchBST(root.left, val)
        else: return self.searchBST(root.right, val)

# Clean recursive BST search
# Time: O(log n)
# Space: O(log n)