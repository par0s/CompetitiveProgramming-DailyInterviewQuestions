class Node:
    def __init__(self):
        self.next = [None] * 26
        self.isEnd = False

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node()
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        head = self.head
        for l in word:
            index = ord(l) - ord('a')
            if head.next[index] == None:
                head.next[index] = Node()
            head = head.next[index]        
        head.isEnd = True        
        
        
class Solution:
    def getIndex(self,letter):
        return ord(letter) - ord('a')
    
    def dfs(self,i,j,node,board,res,curr,n,m):
        # print(curr)        
        if node.isEnd:
            res.add(curr)
            
        headArr = node.next
        neighbours = [(0,1),(1,0),(0,-1),(-1,0)]
        for direction in neighbours:
            newX = i + direction[0]
            newY = j + direction[1]
            if 0 <= newX < n and 0 <= newY < m:            
                if board[newX][newY] != -1:
                    for row in board:
                        print(row)
                    index = self.getIndex(board[newX][newY])
                    if node.next[index] != None:
                        letter = board[newX][newY]                        
                        board[newX][newY] = -1                        
                        self.dfs(newX,newY,node.next[index],board,res,curr + letter,n,m)
                        board[newX][newY] = letter
                            
    
    def findWords(self, board, words):
        trie = Trie()
        for word in words:
            trie.insert(word)
    
        res = set()
        n,m = len(board),len(board[0])
        headArr = trie.head.next                
        for i in range(n):
            for j in range(m):
                index = self.getIndex(board[i][j])
                if headArr[index] != None:     
                    letter = board[i][j]                        
                    board[i][j] = -1                 
                    self.dfs(i,j,headArr[index],board,res,letter,n,m)
                    board[i][j] = letter
            
        return [word for word in res]

soln = Solution()
a = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
b = ["oath","pea","eat","rain"]

a = [["a","b"],["c","d"]]
b = ["abcb"]

a = [["a","a"]]
b = ["aaa"]
print(soln.findWords(a,b))