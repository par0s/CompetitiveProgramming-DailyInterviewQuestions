class Solution:
    def merge(self, intervals):
        if not intervals:
            return []
        
        intervals.sort()
        curr_min = intervals[0][0]
        curr_max = intervals[0][1]
        ans = []

        for i in intervals:
            if i[0] <= curr_max:
                curr_max = max(curr_max,i[1])
            else:
                ans.append([curr_min,curr_max])
                curr_min = i[0]
                curr_max = i[1]
        
        if not ans or intervals[-1][-1] != ans[-1][-1]:
            ans.append([curr_min,curr_max])
        return ans
        