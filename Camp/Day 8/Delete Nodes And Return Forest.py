# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []
        
        to_delete = set(to_delete)
        forest = []
        self.recurDelete(root,to_delete,forest,None)
        
        if root.val not in to_delete:
            forest.append(root)
        
        return forest                

    def recurDelete(self,root,to_delete,forest,parent):
                    
        if root.left:            
            self.recurDelete(root.left,to_delete,forest,root)
            if root.left.val in to_delete:
                root.left = None
        if root.right:
            self.recurDelete(root.right,to_delete,forest,root)
            if root.right.val in to_delete:
                root.right = None
        
        if parent and (root.val not in to_delete and parent.val in to_delete):
            forest.append(root)                    
                
        
        
        
        

            
    
        