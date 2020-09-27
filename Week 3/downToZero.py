def downToZero(n):
    #
    # Write your code here.
    #
    dp = [float('inf')] * (n + 1)
    dp[0],dp[1],dp[2] = 0,1,2

    for i in range(2,n + 1):
        if dp[i] == float('inf') or dp[i] > dp[i - 1] + 1:
            dp[i] = dp[i - 1] + 1
        for j in range(i,n + 1):
            if i * j <= n:
                dp[i * j] = min(dp[j] + 1,dp[i * j])
            else:
                break
        # print(dp)
    return dp[n]

n = 3
n = 12
print(downToZero(n))