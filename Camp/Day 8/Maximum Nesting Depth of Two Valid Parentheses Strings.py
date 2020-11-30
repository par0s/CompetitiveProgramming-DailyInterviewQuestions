class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:        
        n = len(seq)
        res = [0] * n        
        one_c = True
        
        stack = []
        for i in range(n):
            if seq[i] == "(":                
                if not stack or stack[-1][-1] == 0:
                    stack.append(["(",i,1])
                    one_c = False
                else:
                    stack.append(["(",i,0])
            else:
                toPop = stack.pop()
                if toPop[-1] == 1:
                    res[toPop[1]] = 1
                    res[i] = 1
                    one_c = True
                else:
                    res[toPop[1]] = 0
                    res[i] = 0                
        return res
                
                
            
        
        
        