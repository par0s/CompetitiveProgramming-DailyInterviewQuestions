class digit:
    def __init__(self,number):                
        self.stringed = str(number)        
    
    def __gt__(self,digit2):                
        return self.stringed + digit2.stringed > digit2.stringed + self.stringed     
        

class Solution:
    def largestNumber(self, nums):
        smallestNumber = []
        for i in nums:
            i_digit = digit(i)
            smallestNumber.append(i_digit)
        
        smallestNumber.sort()
        largestNumber = []
        for i in smallestNumber:            
            largestNumber.append(i.stringed)
        
        if all([i == "0" for i in largestNumber]):
            return "0"
        return "".join(largestNumber[::-1])