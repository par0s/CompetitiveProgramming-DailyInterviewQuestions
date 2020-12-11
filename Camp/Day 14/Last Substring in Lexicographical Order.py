class Solution:
    def lastSubstring(self, s: str) -> str:     
        maxL = 'a'
        for i in s:
            if i > maxL:
                maxL = i
        
        starts = set()        
        n = len(s)
        for i in range(n):
            if s[i] == maxL:
                firstStart = i                                              
                break
        
        secondStart = -1
        ind = 0        
        i = firstStart + 1
        
        while(i < n):            
            if secondStart != -1:
                if s[secondStart + ind] > s[firstStart + ind]:
                    firstStart = secondStart
                    secondStart = -1
                    ind = 0
                    i = firstStart + 1                    
                elif s[secondStart + ind] < s[firstStart + ind]:
                    ind = 0
                    i = secondStart + 1
                    secondStart = -1                    
                else:
                    ind += 1
                    i += 1
            elif s[i] == maxL:                
                secondStart = i                
                ind = 1
                i += 1
            else:
                i += 1
        
        return s[firstStart:]