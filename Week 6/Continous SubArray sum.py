class Solution:
    def checkSubarraySum(self, num: List[int], k: int) -> bool:                
        n = len(num)                
        k = abs(k)
        prefix  = [num[0] % k if k > 0 else 0]
        
        if n == 1:
            return False
        
        for i in range(1,n):
            j = prefix[-1] + num[i]
            if k > 0:
                prefix.append(j % k)                                    
        
        if k == 0:
            for i in range(1,n):
                if num[i] == num[i - 1] == 0:
                    return True
            return False
        
        mods = set()        
        for pi in range(2,n):
            p = prefix[pi]
            mods.add(prefix[pi - 2])           
            
            if prefix[pi] in mods:
                return True
        
        if k > 0 and prefix[-1] % k == 0:  
            #edge cases for considering the whold array 
            #and if the length is only 2
            return True
        return False
            