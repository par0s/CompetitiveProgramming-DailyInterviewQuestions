class Solution:    
    def corpFlightBookings(self, books: List[List[int]], n: int) -> List[int]:
        res = [0] * (n)
        for i in books:
            res[i[0] - 1] += i[2]
            if i[1] < n:
                res[i[1]] -= i[2]
                
        for i in range(1,n):
            res[i] = res[i - 1] + res[i]
            
        return res
        