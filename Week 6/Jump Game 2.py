class Solution:
    def jump(self, nums: List[int]) -> int:        
        if len(nums) == 1:
            return 0
        
        n,steps = len(nums),0
        
        stack = [(0,0)]
        while(stack):            
            root,steps = stack.pop()
            maxer,ind = 0,root
            for i in range(root + 1,min(root + nums[root] + 1,n)):
                if i + nums[i] > maxer:
                    maxer = i + nums[i]
                    ind = i
                if i == n - 1:
                    # print("#",root,i,i+nums[i])
                    return steps + 1
            stack.append((ind,steps +  1))
        
        return -1