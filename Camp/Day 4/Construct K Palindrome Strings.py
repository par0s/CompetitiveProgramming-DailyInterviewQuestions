import collections
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        f = collections.Counter(s)        
        odd = 0
        for i in f:
            occur = f[i]
            if occur % 2 != 0:
                odd += 1            
        if k < odd or k > len(s):
            return False
        return True
    

                
