class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:     
        self.dp ={}
        return self.findMinLength(s,0,"1",0,k)
    
    def findMinLength(self,s,ind,lastChar,lastCount,kleft):  
        state = (ind,lastChar,lastCount,kleft)
        
        if state in self.dp:
            return self.dp[state]
        
        res = 1000
        if kleft < 0:
            return res
        
        if ind >= len(s):
            return 0
        
        #delete it
        res = min(res,self.findMinLength(s,ind + 1,lastChar,lastCount,kleft - 1))
        
        #use it
        if s[ind] == lastChar:
            subs = min(res,self.findMinLength(s,ind + 1,lastChar,lastCount + 1,kleft))
            if lastCount == 1 or lastCount == 9 or lastCount == 99 or lastCount == 999:
                res = min(res,1 + subs)
            else:
                res = min(res,subs)
        else:
            res = min(res,1 + self.findMinLength(s,ind + 1,s[ind],1,kleft))
        
        self.dp[state] = res
        return res
            
                