class Solution:
    def dfs(self,B,i,j,visited):
        B[i][j] = "#"
        n = len(B)
        m = len(B[0])
        neighbours = [(0,1),(0,-1),(1,0),(-1,0)]
        for neighbour in neighbours:
            new_x = i + neighbour[0]
            new_y = j + neighbour[1]
            if 0 <= new_x < n and 0 <= new_y < m and visited[new_x][new_y] == 0:
                if B[new_x][new_y] == "O":
                    visited[new_x][new_y] = 1
                    self.dfs(B,new_x,new_y,visited)
    
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        
        visited = []
        for _ in range(n):
            visited.append([0 for j in range(m)])
            
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0 or i == n - 1 or j == m - 1 and visited[i][j] == 0:
                    if board[i][j] == "O":
                        visited[i][j] = 1                        
                        self.dfs(board,i,j,visited)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
        
        for row in board:
            print(row)

b = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
s = Solution()        
s.solve(b)
        