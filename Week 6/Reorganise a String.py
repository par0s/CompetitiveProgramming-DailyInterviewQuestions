    import heapq
class Solution:
    def reorganizeString(self, S: str) -> str:
        if len(S) == 1:
            return S
        
        dicts = {}                        
        for i in S:
            if i in dicts:
                dicts[i] += 1
            else:
                dicts[i] = 1
                
        heap = []
        for letter in dicts:
            heapq.heappush(heap,(-dicts[letter],letter))
        
        result = ""        
        # The idea behind the following algorithm is to reach to a point where all the frequency
        # left after some steps is the same which is easy to order with no same neighbours
        # eg: "aaabbbcd" reduced to "abab + " " left with frequency of all left with 1
        while(heap):            
            count,most = heapq.heappop(heap)
            result += most
            count *= -1            
            
            if not heap and count > 1:
                return ""
            if not heap and count == 1:
                return result
            
            count2,most2 = heapq.heappop(heap)            
            result += most2
            count2 *= -1
            
            count -= 1
            count2 -= 1
            if count > 0:
                heapq.heappush(heap,(-count,most))
            if count2 > 0:
                heapq.heappush(heap,(-count2,most2))
        
        return result
            
            
        
        
        
            