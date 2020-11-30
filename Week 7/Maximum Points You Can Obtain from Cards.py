class Solution:
    def maxScore(self, card: List[int], k: int) -> int:
        n = len(card)
        suffix_sum = [card[-1]]
        for i in range(n - 2,-1,-1):
            suffix_sum.append(card[i] + suffix_sum[-1])
        
        prefix_sum = [card[0]]
        for i in range(1,n):
            prefix_sum.append(card[i] + prefix_sum[-1])
                
        if k == n:
            return prefix_sum[-1]
        
        res = suffix_sum[k - 1]
        
        for i in range(min(k,i)):
            curr = prefix_sum[i]
            if i < k - 1:
                curr += suffix_sum[k - (i + 1) - 1]
            # print(i,curr)
            res = max(res,curr)
                        
        return res
                
        