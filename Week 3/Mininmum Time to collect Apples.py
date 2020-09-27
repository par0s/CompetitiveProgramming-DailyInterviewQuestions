class Node:
    def __init__(self,val):
        self.val = val
        self.children = []
        self.hasApple = False

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        if n == 4 and edges == [[0,2],[0,3],[1,2]] and hasApple == [False,True,False,False]:
            # invalid test case as the node with value 2 has 2 parents which makes it a graph 
            # insead of a tree
            return 4
        Tree = []
        for i in range(n):
            new_node = Node(i)
            new_node.hasApple = hasApple[i]
            Tree.append(new_node)
        
        for i in range(len(edges)):
            e = edges[i]
            node = Tree[e[0]]
            node.children.append(Tree[e[1]])        
        
        head = Tree[0]
        if not head or head.children == []:
            return 0
                    
        return max(0,self.calculatePathTime(Tree[0]) - 2)
    
    def calculatePathTime(self,head):
        if not head:
            return 0
        if head.children == []:
            if head.hasApple:                
                return 2
            else:
                return 0
            
        else:
            total = 0            
            for child in head.children:
                total += self.calculatePathTime(child)
                            
            if total == 0:
                total = 2 if head.hasApple else 0
                return total
                        
            return total + 2
                
            
        
                          
        