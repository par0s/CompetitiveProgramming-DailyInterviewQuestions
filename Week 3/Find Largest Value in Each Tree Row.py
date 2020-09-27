# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        queue = [(root,0)]
        res = []
        
        curr_big,curr_level = float('-inf'),0
        while(queue):
            # print(1)
            root,level = queue.pop(0)
            if level == curr_level:
                curr_big = max(curr_big,root.val)
            else:
                res.append(curr_big)
                curr_level += 1
                curr_big = root.val
            
            # print(root.val,curr_level,curr_big)
            if root.left:
                queue.append((root.left,level + 1))
            if root.right:
                queue.append((root.right,level + 1))
        
        res.append(curr_big)
        return res
                
            
            
        