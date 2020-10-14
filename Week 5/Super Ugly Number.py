import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        uglies = [1]
        ugly_count = 0     
        visited = set()
        
        while(ugly_count < n):      
            # print(uglies)
            next = heapq.heappop(uglies)            
            ugly_count += 1
            if ugly_count == n:
                return next
            for i in primes:
                next_ugly_number = next * i    
                if next_ugly_number not in visited:
                    heapq.heappush(uglies,next_ugly_number)                
                visited.add(next_ugly_number)
        return 1
                