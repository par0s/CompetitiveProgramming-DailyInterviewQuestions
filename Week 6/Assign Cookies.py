import heapq
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        heapq.heapify(s)                
        ans = 0
        for i in g:
            while(s):
                candy = heapq.heappop(s)
                if candy >= i:
                    ans += 1
                    break
            else:
                return ans
        
        return ans
    
        