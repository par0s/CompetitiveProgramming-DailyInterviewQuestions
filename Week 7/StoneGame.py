class Solution:
    def stoneGame(self, arr: List[int]) -> bool:
        total = sum(arr)
        half = total // 2
        
        n = len(arr)
        dp = []
        for i in range(n):
            dp.append([0 for i in range(n)])

        for s in range(n):
            for r in range(n):
                if r + s < n:
                    if s == 0:
                        dp[r][r] = arr[r]
                    elif s == 1:
                        dp[r][r + s] = max(arr[r],arr[r + s])
                    else:
                        first = arr[r] + min(dp[r + 2][r + s],dp[r + 1][r + s - 1])
                        second = arr[r + s] + min(dp[r + 1][r + s - 1],dp[r][r + s - 2])
                        dp[r][r + s] = max(first,second)
        
        return dp[0][-1] > half
            
                
                
        
        
        