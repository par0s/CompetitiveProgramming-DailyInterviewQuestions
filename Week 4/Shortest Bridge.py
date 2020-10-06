class Solution:
    def shortestBridge(self, B):
        visited = []
        n = len(B)
        m = len(B[0])
        first = True

        for _ in range(n):
            visited.append([0 for j in range(m)])
        
        for i in range(n):
            for j in range(m):
                if B[i][j] == 1:
                    visited[i][j] = 1
                    if first:                        
                        self.dfs(B,i,j,"a",visited)
                        first = False
                    else:
                        self.dfs(B,i,j,"b",visited)
        
        visited = []
        for _ in range(n):
            visited.append([0 for j in range(m)])

        queue = []
        neighbours = [(0,1),(0,-1),(1,0),(-1,0)]        
        for i in range(n):
            for j in range(m):
                if B[i][j] == "a":
                    for neighbour in neighbours:
                        new_x = i + neighbour[0]
                        new_y = j + neighbour[1]
                        if 0 <= new_x < n and 0 <= new_y < m and B[new_x][new_y] == 0 and visited[new_x][new_y] == 0:
                            queue.append([new_x,new_y])
                            B[new_x][new_y] = 1
                            visited[new_x][new_y] = 1        
        while(queue):
            i,j = queue.pop(0)
            for neighbour in neighbours:
                new_x = i + neighbour[0]
                new_y = j + neighbour[1]
                if 0 <= new_x < n and 0 <= new_y < m and  B[new_x][new_y] != "a" and visited[new_x][new_y] == 0:
                    if B[new_x][new_y] == "b":
                        # print(B[i][j])
                        return B[i][j]  
                    elif B[new_x][new_y] == 0:  
                        B[new_x][new_y] = B[i][j] + 1                                      
                        queue.append([new_x,new_y])
                        visited[new_x][new_y] = 1
        
        return -1
                        
    def dfs(self,B,i,j,mark,visited):
        B[i][j] = mark
        n = len(B)
        m = len(B[0])
        neighbours = [(0,1),(0,-1),(1,0),(-1,0)]
        for neighbour in neighbours:
            new_x = i + neighbour[0]
            new_y = j + neighbour[1]
            if 0 <= new_x < n and 0 <= new_y < m and B[new_x][new_y] == 1 and visited[new_x][new_y] == 0:
                visited[new_x][new_y] = 1
                self.dfs(B,new_x,new_y,mark,visited)

        
        