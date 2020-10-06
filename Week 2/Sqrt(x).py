import math
class Solution:        
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x < 3:
            return 1
        
        low = 0
        high = x
        while(low < high):
            mid = (low + high) // 2
            midSquared = mid ** 2
            
            if midSquared > x:
                high = mid
            elif midSquared < x:
                low = mid + 1
            
            if midSquared > x and (mid - 1) ** 2 < x:
                return mid - 1
            
            if midSquared == x:
                return mid
        
        return -1
        
        