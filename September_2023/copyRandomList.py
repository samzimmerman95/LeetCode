"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
"""
Prompt
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # First create a copy of the linked list with only the next pointer
        # Create a dictionary with key of original node pointing to deep copy of that node
        # Second pass through original list find current node's random pointed to Node in dictionary
        # and associate it's value with current deep copy's random pointer
        d = {}
        deep = Node(head.val)
        deep_pointer = deep
        d[head] = deep_pointer
        old_pointer = head.next
        
        while old_pointer != None:
            deep_pointer.next = Node(old_pointer.val)
            deep_pointer = deep_pointer.next
            d[old_pointer] = deep_pointer
            old_pointer = old_pointer.next

        deep_pointer = deep
        old_pointer = head
        while old_pointer != None:
            if old_pointer.random:
                deep_pointer.random = d[old_pointer.random]
            deep_pointer = deep_pointer.next
            old_pointer = old_pointer.next

        return deep
