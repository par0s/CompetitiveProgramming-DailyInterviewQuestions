class Solution:
    def maxSatisfaction(self, st: List[int]) -> int:
        st.sort()
        n = len(st)
        taken = [0] * n
        maxer = 0
        for i in range(n - 1,-1,-1):
            for j in range(i,n):
                taken[j] += st[j]            
            maxer = max(maxer,sum(taken))
        
        return maxer
    
    def maxSatisfactionBetter(self, st: List[int]) -> int:
        st.sort(reverse = True)
        n = len(st)
        res = 0
        current_add = 0
        for i in range(n):
            if st[i] + current_add <= 0:
                break
            current_add += st[i]
            res += current_add
        
        return res
        
    
            
