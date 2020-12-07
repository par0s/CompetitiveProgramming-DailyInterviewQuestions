class Solution:
    def getAsciiSum(self,strs):
        total = 0
        for i in strs:
            total += ord(i)
        return total
    
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        #finding lcs
        dp = []
        n,m = len(s1),len(s2)
        
        for i in range(n):
            dp.append([0 for j in range(m)])
                    
        maxSubSum = 0
        for i in range(n):
            for j in range(m):
                maxAscii = 0
                if i > 0:
                    maxAscii = max(maxAscii,dp[i - 1][j])
                if j > 0:
                    maxAscii = max(maxAscii,dp[i][j - 1])
                if s1[i] == s2[j]:
                    if i > 0 and j > 0:
                        maxAscii = max(maxAscii,dp[i - 1][j - 1] + ord(s1[i]))
                    else:
                        maxAscii= max(maxAscii,ord(s1[i]))
                
                dp[i][j] = maxAscii                
        
        s1AsciiSum = self.getAsciiSum(s1)
        s2AsciiSum = self.getAsciiSum(s2)
        
        return s1AsciiSum + s2AsciiSum - (2 * (dp[-1][-1]))
            
        
        
                
                
                
                        
                    
                    
                    
                            
                                        
                            
                        