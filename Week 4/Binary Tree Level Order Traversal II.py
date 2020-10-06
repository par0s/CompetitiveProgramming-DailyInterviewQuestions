# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [(root,0)]
        res = []
        curr_row = []
        curr_height = 0
        
        while(queue):
            root,height = queue.pop(0)
            if height > curr_height:
                res.append(curr_row)
                curr_height += 1
                curr_row = []
                        
            curr_row.append(root.val)
            # print(curr_row,root.val,"height = ",height,"curr = ",curr_height)
            if root.left:
                queue.append((root.left,height + 1))
            if root.right:
                queue.append((root.right,height + 1))
        
        if curr_row:
            res.append(curr_row)
        return res[::-1]
                                

                
            
        
        