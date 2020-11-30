class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        dp = []
        r = len(mat)
        c = len(mat[0])
        
        for i in range(r):
            row = []
            for j in range(c):
                if mat[i][j] == 1:
                    row.append([1,1])
                else:
                    row.append([0,0])
            dp.append(row)
        
        res = 0
        
        for i in range(r):
            for j in range(c):
                if j > 0 and mat[i][j] == 1 and mat[i][j - 1] == 1:
                    dp[i][j][0] = dp[i][j - 1][0] + 1
                    
                if i > 0 and mat[i][j] == 1 and mat[i - 1][j] == 1:
                    dp[i][j][1] = dp[i - 1][j][1] + 1
                
        
        # 1 + 1 + (1 + 1) + ()
        ans = 0
        for row in dp:
            print(row)
            for cell in row:
                ans += (cell[0] + cell[1])
                print(cell[0] * cell[1],end = "        ")
            print()
        
        return ans
                
# [[1,1,1],[1,1,1],[1,1,1]]
#[[0,1,1,0],
# [0,1,1,1],
# [1,1,1,0]] 