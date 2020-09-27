# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.ind = 0
        self.arr = []
        self.popper(root)
    
    def popper(self,head):
        if not head:
            return
        self.popper(head.left)
        self.arr.append(head.val)
        self.popper(head.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        ans = self.arr[self.ind]
        self.ind += 1
        return ans
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.ind < len(self.arr):
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()