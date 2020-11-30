class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        #first use binary search to find the array it could be in
        arrayIndex = self.findArrayIndex(matrix,target)
        
        if arrayIndex == -1:
            return False
    
        # print(arrayIndex)
        #then use binary serach to find if it exists on that array
        arr = matrix[arrayIndex]        
        bs = self.binary_search(arr,target)
        
        if bs != -1:
            return True
        return False
        
    def binary_search(self,arr, x): 
        low = 0
        high = len(arr) - 1
        mid = 0
        
        while(low <= high):
            mid = (low + high) // 2
            if arr[mid] < x:
                low = mid + 1
            elif arr[mid] > x:
                high = mid - 1
            else:
                return mid        
        return -1
    
    def findArrayIndex(self,matrix,target):
        lb = 0
        hb = len(matrix) - 1
        
        if len(matrix[lb]) == 0 or len(matrix[hb]) == 0:
            return -1
        
        if target <= matrix[lb][-1]:
            return lb
        if target > matrix[hb][-1]:
            return -1
        
        while(lb < hb):
            mid = (lb + hb) // 2 
            if target > matrix[mid][-1]:
                lb = mid + 1
            else:
                hb = mid
            
            if lb == hb:
                if matrix[lb][-1] <= target:
                    return lb
                else:
                    return hb                
        return -1
    

            
        