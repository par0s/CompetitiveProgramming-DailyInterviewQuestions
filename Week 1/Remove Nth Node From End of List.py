# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n,ind = 0,prev = None):
        fill = []        
        while(head):            
            fill.append(head)
            head = head.next
        
        realInd = len(fill) - n
        if realInd == 0:
            if len(fill) > 1:
                return fill[1]
            else:
                return None
        else:            
            deleteNext = fill[realInd].next            
            fill[realInd - 1].next = deleteNext
        
        return fill[0]
                
        