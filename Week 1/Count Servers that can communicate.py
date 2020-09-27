class Solution:
    def countServers(self, grid):
        m = len(grid)
        n = len(grid[0])
        rowCheck = [0 for i in range(m)]
        columnCheck = [0 for i in range(n)]
        ans = 0
        
        doubleCheck = []
        for i in range(m):
            doubleCheck.append([0 for i in range(n)])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if rowCheck[i] or columnCheck[j]:                    
                        ans += 1
                        doubleCheck[i][j] = True
                    rowCheck[i] += 1 
                    columnCheck[j] += 1
        
        for i in range(m):
            for j in range(n):
                if (rowCheck[i] > 1 or columnCheck[j] > 1) and grid[i][j] == 1 and doubleCheck[i][j] == False:
                    ans += 1
        
        return ans
                