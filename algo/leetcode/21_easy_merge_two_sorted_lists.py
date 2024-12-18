# Top Interview 150 : 2024-12-18
# https://leetcode.com/problems/merge-two-sorted-lists


from types import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getNext(self, node1, node2):
        if not node1 and not node2:
            assert False
        if not node1:
            return node2, node1, node2.next
        if not node2:
            return node1, node1.next, node2
        if node1.val > node2.val:
            return node2, node1, node2.next
        if node1.val <= node2.val:
            return node1, node1.next, node2
        assert False

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        merged_list = merged_head = None
        while list1 or list2:
            next_node, list1, list2 = self.getNext(list1, list2)
            if not merged_list:
                merged_list = merged_head = ListNode(next_node.val)
                continue

            merged_head.next = ListNode(next_node.val)
            merged_head = merged_head.next

        return merged_list


# Time: O(n)
# Space: O(1)
