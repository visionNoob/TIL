# Daily Question: 2024-12-20
# 2415. Reverse Odd Levels of Binary Tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import Optional


# its my first solution, but it is so slow
class Solution1:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        stack_l = deque([(root, 0)])
        stack_r = deque([(root, 0)])

        table = {}
        while stack_l:
            node_l, level = stack_l.popleft()
            node_r, level = stack_r.popleft()
            table[level] = table.get(level, 0) + 1

            if level % 2 == 1 and table[level] <= (2**level) // 2:
                node_l.val, node_r.val = node_r.val, node_l.val

            if node_l.left:
                stack_l.append((node_l.left, level + 1))
                stack_l.append((node_l.right, level + 1))

                stack_r.append((node_r.right, level + 1))
                stack_r.append((node_r.left, level + 1))
        return root


# Time: O(n)
# Space: O(n)


# inspired by https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/solutions/2594787/python-3-11-lines-queue-t-s-84-70
class Solution2:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        queue, level = deque([(root)]), 0

        while queue[0]:

            if level:
                for i in range(len(queue) >> 1):
                    queue[i].val, queue[-1 - i].val = queue[-1 - i].val, queue[i].val

            for _ in range(len(queue)):
                node = queue.popleft()
                queue.append(node.left)
                queue.append(node.right)

            level ^= 1

        return root


# Time: O(n)
# Space: O(n)
