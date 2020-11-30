def optimal(arr):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return max(arr[0],arr[1])
    else:
        n = len(arr)
        ans1 =  arr[0] + min(optimal(arr[2:]),optimal(arr[1:n - 1]))
        ans2 = arr[n - 1] + min(optimal(arr[1:n - 1]),optimal(arr[:n - 2]))     
        print(arr,ans1,ans2)           
        return max(ans1,ans2)

def optimalBottomUp(arr):
    n = len(arr)
    dp = []
    for i in range(n):
        row = []
        for r in range(n):
            row.append(0)
        dp.append(row)
    
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
    for row in dp:
        print(row)


arr = [5, 3, 7, 10]
arr = [8, 15, 3, 7]
# 1 2 3 4 5 6 
arr = [3,7,3,2,5,1,6,3,10,7]
# print(sum)
print(optimalBottomUp(arr))
    
