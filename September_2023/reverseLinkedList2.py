# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
92. Reverse Linked List II
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
"""
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        def reverse(head):
            # A function that reverses a linked list
            prev = None
            after = None
            current = head

            while current:
                after = current.next
                current.next = prev
                prev = current
                current = after
            
            return prev

        # Find the left, center and right sections and splits them up, reverses the center then glues them back together
        if left == right:
            return head

        left_section = None
        if left != 1:
            left_section = head
        right_section = None
        reverse_section = None
        traverse = head
        counter = 1
        while traverse:
            if counter == left:
                reverse_section = traverse
            if counter == right:
                right_section = traverse.next
                traverse.next = None
            traverse = traverse.next
            counter += 1

        # print(left_section)
        # print(reverse_section)
        # print(right_section)

        reversed_section = reverse(reverse_section)
        traverse = head
        counter = 1
        if left_section:
            while counter + 1 < left:
                traverse = traverse.next
                counter += 1
            traverse.next = reversed_section
        else:
            traverse = reversed_section
            head = traverse
        
        while traverse:
            if traverse.next == None:
                traverse.next = right_section
                break;
            else:
                traverse = traverse.next
        

        return head

        # This is by no means the most optimal solution. 

        # You can do a pretty clever operation with three pointers.
        # Find where the reversing needs to start. Basically putting next in front of previous
        # if left == right:
        #     return head

        # dummy = ListNode(0, head)
        # prev = dummy

        # for i in range(left-1):
        #     prev = prev.next
        
        # current = prev.next

        # for i in range(right - left):
        #     next_node = current.next
        #     current.next = next_node.next
        #     next_node.next = prev.next
        #     prev.next = next_node
        
        # return dummy.next


        