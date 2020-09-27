# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, dest,res = [],currSum = 0,coll = []) -> List[List[int]]:
        if not root and res == []:
            return []
        
        if root and root.left == None and root.right == None:
            if currSum + root.val == dest:
                ansColl = coll[:]
                ansColl.append(root.val)
                res.append(ansColl)
        elif root:
            currSum += root.val
            newColl = coll[:]
            newColl.append(root.val)
            if root.left:
                self.pathSum(root.left,dest,res,currSum,newColl)
            if root.right:
                self.pathSum(root.right,dest,res,currSum,newColl)
        soln = res[:]
        return soln
        