class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        #state - jump,lane,col
        #moves - straight,any col beside self
        
        board,n = [],len(obstacles)
        for i in range(n):
            board.append([float(inf)] * 3)
        
        board[0][1] = 0
        
        for i in range(n - 1):            
            for j in range(3):
                lanes = [0,1,2]
                for l in lanes:
                    if obstacles[i] != l + 1:                        
                        board[i][l] = min(board[i][l],board[i][j] + 1)
                        
            for j in range(3):
                if obstacles[i + 1] != j + 1:
                    board[i + 1][j] = min(board[i + 1][j],board[i][j])
                    
        return min(board[-1][0],board[-1][1],board[-1][2])
