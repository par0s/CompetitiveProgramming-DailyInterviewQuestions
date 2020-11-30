class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        if target > nums[-1]:
            return high + 1
        
        if target < nums[0]:
            return 0 
        
        while(low <= high):
            mid = (low + high) // 2            
            
            if nums[mid] > target:
                high = mid - 1                
            elif nums[mid] < target:
                low = mid + 1                 
            else:
                return mid  
                
        if nums[low] < target:
            return low + 1
        else:
            return low 
        
        
        
        
        