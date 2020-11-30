class Solution:
    def isPossible(self, nums):        
        not_taken = {}
        
        for i in nums: 
            if i in not_taken:
                not_taken[i] += 1
            else:
                not_taken[i] = 1
            if i + 1 not in not_taken:
                not_taken[i + 1] = 0
            if i + 2 not in not_taken:
                not_taken[i + 2] = 0
                
        ends = {}
        
        for i in nums:
            # print(not_taken,ends,i)
            if not_taken[i] > 0:                                
                not_taken[i] -= 1
                if i - 1 in ends and ends[i - 1] > 0:
                    ends[i - 1] -= 1
                    if i in ends:
                        ends[i] += 1                
                    else:
                        ends[i] = 1

                elif not_taken[i + 1] > 0 and not_taken[i + 2] > 0:                
                    not_taken[i + 1] -= 1
                    not_taken[i + 2] -= 1
                    if i + 2 in ends:
                        ends[i + 2] += 1                
                    else:
                        ends[i + 2] = 1
                else:
                    return False
                        
        return True              
        
# [1,2,3,3,4,4,5,5]
# [1,2,5,5,6,6,7,8,8,9]
# [1,2,3,3,4,4,5,5]
# [1,2,3,4,4,5]    
# [4,5,6,7,7,8,8,9,10,11]
        
            
        