import math
class Solution:
    def countBits(self, num: int):
        if num == 0:
            return [0]
        elif num == 1:
            return [0,1]
        
        dp = [0] * (num + 1)        
        last = 2
        dp[1] = 1
        dp[2] = 1
        
        for i in range(3,num + 1):            
            if i == (last * 2):
                last = i
                dp[i] = 1
            else:
                dp[i] = dp[last] + dp[i - last]        
        return dp
            
            
        