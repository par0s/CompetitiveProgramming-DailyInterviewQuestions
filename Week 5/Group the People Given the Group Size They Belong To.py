class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        n = len(groupSizes)
        
        for i in range(n + 1):
            groups[i] = []
        
        for p in range(len(groupSizes)):
            size = groupSizes[p]
            
            if len(groups[size]) == 0:
                groups[size].append([p])
            else:
                if len(groups[size][-1]) != size:
                    groups[size][-1].append(p)
                else:
                    groups[size].append([p])
        
        res = []
        for size in groups:
            for group in groups[size]:
                if len(group) != 0:
                    res.append(group)
                
        return res
                    
        
        