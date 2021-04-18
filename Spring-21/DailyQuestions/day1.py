class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:             
        n = len(names)
        taken = {}        
        counter = {}
        for name in names:
            counter[name] = 1
            taken[name] = set()
                
        result = []
        visited = set()
        for name in names:
            if name not in visited:                
                result.append(name)
                visited.add(name)
            else:             
                corrected = f'{name}({counter[name]})'
                while(corrected in visited):
                    counter[name] += 1 
                    corrected = f'{name}({counter[name]})'                    
                                
                result.append(corrected)
                visited.add(corrected)
                counter[name] += 1                
                counter[corrected] = 1
                taken[corrected] = set()
                    
        return result        
        
        
        
        
        
        
        
        
        
        
        
        
        