class Solution:
    def mostCompetitive(self, nums, k):
        deque = []
        n = len(nums)
        res = []
        
        for i in range(n):            
            while(deque and nums[i] < deque[-1]):
                deque.pop()
            deque.append(nums[i])
            print(i,deque)
            if n - i <= k:
                res.append(deque.pop(0))
        while(deque and len(res) < k):
            res.append(deque.pop(0))

        # print(res)
        return res
            

s = Solution()
n = [3,5,2,6]
k = 2
n = [71,18,52,29,55,73,24,42,66,8,80,2]
k = 3
s.mostCompetitive(n,k)