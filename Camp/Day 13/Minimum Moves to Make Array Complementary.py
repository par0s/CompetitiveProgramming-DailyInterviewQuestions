class Solution:
    def minMoves(self, nums, limit):
    	n = len(nums)
    	maxPairs = set()
    	minPairs = set()
    	for i in range(n):
    		maxPairs.add(max(nums[i],nums[n - i - 1]))
    		minPairs.add(min(nums[i],nums[n - i - 1]))

    	print(maxPairs)
    	print(minPairs)

nums = [1,2,3,4]
l = 4
s = Solution()
s.minMoves(nums,l)


        