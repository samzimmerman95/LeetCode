# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
725. Split Linked List in Parts
Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.
The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.
The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.
Return an array of the k parts.
"""
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        # Count the length of the array
        current = head
        length = 0
        while current:
            length += 1
            current = current.next

        # Determine the length of each piece when splitting the length into k parts, accounting for size difference
        base = length // k
        extra = length % k
        pieces = []
        for i in range(k):
            part_length = base
            if extra:
                part_length += 1
                extra -= 1
            pieces.append(part_length)

        current = head
        remainding = None
        output = [None]*k

        # Split list into sections of their determined lengths and assign to array. Using two pointers to not lose track of location
        for i in range(k):
            part_length = pieces[i]
            output[i] = current

            while part_length >= 1:
                if part_length == 1:
                    remainder = current.next
                    current.next = None
                    current = remainder
                else:
                    current = current.next
                part_length -= 1
                
        return output
        