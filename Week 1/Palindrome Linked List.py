################################################# Solution 1 #################################################
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head):
        reversed = self.reverseLinked(head)
        res = self.check(head,reversed)
        
        print(head)
        print(reversed)
        return res
    
    def check(self,head,reversed):        
        if head == None and reversed == None:
            return True
        if (head and reversed) and head.val == reversed.val:            
            return self.check(head.next,reversed.next)          
        return False  
        
    
    def reverseLinked(self,head,previous = None):
        if not head.next:
            reverseHead = ListNode(head.val)            
            reverseHead.next = previous
            return reverseHead
        else:
            newNode = ListNode(head.val)
            newNode.next = previous
            return self.reverseLinked(head.next,newNode)
        
        
################################################# Solution 2 #################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fill = []
        headInd = head
        
        while(head):            
            fill.append(head)
            head = head.next
        
        reversed = fill[::-1]
        
        for i in range(len(fill)):
            if fill[i].val != reversed[i].val:
                return False
        
        return True