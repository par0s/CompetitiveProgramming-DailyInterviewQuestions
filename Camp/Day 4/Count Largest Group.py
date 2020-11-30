class Solution:
    def digSize(self,n):        
        res = 0
        while(n > 0):
            res += n % 10
            n = n // 10
        return res
        
    def countLargestGroup(self, n: int) -> int:        
        count = {}
        largestSize = 1
        for i in range(1,n + 1):
            t = self.digSize(i)             
            if t in count:
                count[t] += 1
                largestSize = max(largestSize,count[t])
            else:
                count[t] = 1
                
        maxer = 0
        for i in count:
            if count[i] == largestSize:
                maxer += 1
        
        return maxer
