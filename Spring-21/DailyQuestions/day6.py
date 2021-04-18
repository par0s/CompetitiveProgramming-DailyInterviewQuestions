from decimal import Decimal
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        """0.5,1,2
           0.6,3,5
           1.0,2,2
        """
        heap = [[(c[0] / c[1]) - ((c[0] + 1) / (c[1] + 1)),c[0] + 1,c[1] + 1,ind] for ind,c in enumerate(classes)]
        heapq.heapify(heap)
                
        while(extraStudents):                        
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
        for c in classes:
            total += c[0] / c[1]
        return total / len(classes)
            
            
        
        