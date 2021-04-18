def findDist(node,tree,visited):
    maxDist = 1  
    maxSeen = 1  
    cds = []
    for child in tree[node]:
        if child not in visited:
            visited.add(child)
            childDist,childSeen = findDist(child,tree,visited)
            maxDist = max(maxDist,childDist + 1)
            maxSeen = max(maxSeen,childSeen) 
            cds.append(childDist)       
    
    if len(cds) > 1:
        cds.sort()             
        maxSeen = max(maxSeen,cds[-1] + cds[-2] + 1)        
    
    maxSeen = max(maxSeen,maxDist)    
    return maxDist,maxSeen


def solve(spiders):
    dist = 0
    for spider in spiders:        
        N = spider[0]

        edges = []
        for i in range(1,len(spider),2):
            edges.append([spider[i],spider[i + 1]])
        
        tree = {}
        for e in range(1,N + 1):
            tree[e] = set()

        for e in edges:            
            tree[e[0]].add(e[1])    
            tree[e[1]].add(e[0])            
                    
        visited = set()
        visited.add(1)
        x,y = findDist(1,tree,visited)           
        dist += y - 1

    return dist          

def main():
    f = open("input.txt", "r")
    t = int(f.readline())        
    spiders = []
    for _ in range(t):
        d = f.readline()
        d = [int(i) for i in d.split()]
        spiders.append(d)
    ans = str(solve(spiders))

    file1 = open("output.txt", "w")  # write mode
    file1.write(ans)
    file1.close()
 
main()



