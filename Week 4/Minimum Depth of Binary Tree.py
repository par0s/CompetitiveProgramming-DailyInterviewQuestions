# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root, height = 1):
        if not root:
            return 0
        
        if not root.left and not root.right:
            return height
        
        left = float('inf')
        right = left
        
        if root.left:
            left = min(left,self.minDepth(root.left,height + 1))
        if left > height + 1 and root.right:
            right = min(right,self.minDepth(root.right,height + 1))
        
        return min(left,right)
        