class Solution:
    def isPossibleDivide(self, nums,k):
        frequency = {}        
        if len(nums) == 1:
            return True
        
        uniqueValues = set(nums)
        uniqueArray = []
        for i in uniqueValues:
            uniqueArray.append(i)
        uniqueArray.sort()
        
        for i in nums:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
        
        queue = []
        for i in uniqueArray:            
            if not queue:                
                queue.append(i)
            else:                
                if len(queue) == k:
                    first = frequency[queue[0]] 
                    last = queue[0]
                    for l in range(k):
                        s = queue[l]
                        frequency[s] -= first
                        if frequency[s] == 0:                            
                            last = l                            
                    queue = queue[last + 1:] if last < k - 1 else []
                          
                if (queue and frequency[i] < frequency[queue[-1]])  or (queue and i > queue[-1] + 1):
                    return False                
                queue.append(i)            
        
        if len(queue) == k:
            first = frequency[queue[0]] 
            last = queue[0]
            for l in range(k):
                s = queue[l]
                frequency[s] -= first
                if frequency[s] == 0:                            
                    last = l                            
            queue = queue[last + 1:] if last < k - 1 else []
                
        return len(queue) == 0