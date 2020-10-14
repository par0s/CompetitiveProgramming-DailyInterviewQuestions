import heapq
def cookies(k, A):
    #
    # Write your code here.
    #
    a_limit = 5500
    arr = [0] * a_limit
    steps = 0
    miner = a_limit
    
    heapq.heapify(A)

    if min(A) >= k:
        return 0    
    
    if len(A) == 1:
        return -1
    
    first,second = heapq.heappop(A),heapq.heappop(A)
    while(first < k):
        next = first + (second * 2)
        steps += 1
        heapq.heappush(A,next)
        if len(A) == 1 :
            if A[0] >= k:
                return steps
            else:
                return -1
        first,second = heapq.heappop(A),heapq.heappop(A)
    
    return steps if steps > 0 else -1
        
        
    

k = 7 
A = [1,2,3,9,10,12]

# k = 90
# A = [13, 47, 74, 12, 89, 74, 18, 38]
#     [38,47,74,89,74,18,38]
#     [94,47,74,89,74]
#     [94,195,89]
k = 10
A = [1,1,1]

print(cookies(k,A))