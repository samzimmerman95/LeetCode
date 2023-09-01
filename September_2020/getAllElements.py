# Day 05

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        def traverse(root, l):
            if root:
                traverse(root.left, l)
                l.append(root.val)
                traverse(root.right, l)

        l1 = []
        l2 = []
        traverse(root1, l1)
        traverse(root2, l2)
        l1 += l2
        l1.sort()
        return l1
