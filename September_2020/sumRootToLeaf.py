# Day 08

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traverse(r, curNum):
            rootToLeaf = 0
            if r:
                curNum = (curNum << 1) | r.val
                if not (r.left or r.right):

                    rootToLeaf += curNum
                    return rootToLeaf
                if r.left and not r.right:
                    return traverse(r.left, curNum)
                elif not r.left and r.right:
                    return traverse(r.right, curNum)
                else:
                    return traverse(r.left, curNum) + traverse(r.right, curNum)

        return traverse(root, 0)
