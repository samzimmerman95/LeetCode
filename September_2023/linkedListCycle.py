# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
141. Linked List Cycle
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Hash Map solution
        # visited = {}
        # current = head

        # while current:
        #     if current in visited:
        #         return True
        #     visited[current] = True
        #     current = current.next
        
        # return False

        # Two Pointer solution
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False