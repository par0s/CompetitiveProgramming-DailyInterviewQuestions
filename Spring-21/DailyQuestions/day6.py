from collections import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:        
        heap = []                        
        
        for ind,c in enumerate(classes):
            ave = c[0] / c[1]                
            ave2 = (c[0] + 1) / (c[1] + 1)            
            heapq.heappush(heap,[(ave - ave2),c[0] + 1,c[1] + 1,ind])
        
        while(extraStudents > 1):                        
            least = heapq.heappop(heap)            
            i = least[-1]                      
            classes[i][0] = least[1]
            classes[i][1] = least[2]            
            least[1] += 1
            least[2] += 1                        
            least[0] = (classes[i][0]/classes[i][1]) - (least[1]/least[2])
            heapq.heappush(heap,least)
            extraStudents -= 1
        
        total = 0
        for c in heap:
            total += c[1] / c[2]
        return total / len(classes)
            
                        