# leetcode 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list


from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Method 1: Iterative Version
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head

        prev = None
        cur = head
        next = head.next

        while True:

            cur.next = prev

            if not next:
                break
            prev = cur
            cur = next
            next = next.next
        return cur

# Three pointers approach: prev, cur, next
# Time: O(n)
# Space: O(1)


# Method 2: Recursion Version v1
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head

        def reverse(prev, cur, next):
            cur.next = prev
            if not next:
                return cur
            else:
                prev = cur
                cur = next
                next = next.next
                return reverse(prev, cur, next)
        return reverse(None, head, head.next)

# Recursive approach with three parameters
# Time: O(n)
# Space: O(n)


# Method 3: Recursion Version v2
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev(
            prev: Optional[ListNode], cur: Optional[ListNode]
        ) -> Optional[ListNode]:
            if not cur:
                return prev
            nxt = cur.next  # <- 매개변수로 받지 않고 지역변수로만 사용
            cur.next = prev
            return rev(cur, nxt)

        return rev(None, head)

# Cleaner recursive approach with local variable
# Time: O(n)
# Space: O(n)