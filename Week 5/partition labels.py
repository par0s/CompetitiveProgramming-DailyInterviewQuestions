class Solution:
    def partitionLabels(self, S):
        n = len(S)
        lastIndexOccurance = [] 
        for i in range(26):
            lastIndexOccurance.append([n,0,0])
            
        for i in range(n):
            # finding the first and last occurance index of every letter
            lastIndexOccurance[ord(S[i]) % ord("a")][0] = min(lastIndexOccurance[ord(S[i]) % ord("a")][0],i) 
            lastIndexOccurance[ord(S[i]) % ord("a")][1] = max(lastIndexOccurance[ord(S[i]) % ord("a")][1],i) 
            lastIndexOccurance[ord(S[i]) % ord("a")][2] = 1
        
        ranges = []
        for i in range(26):
            new_ranges = []            
            if lastIndexOccurance[i][2] == 1:
                current_max_merged = [lastIndexOccurance[i][0],lastIndexOccurance[i][1]]                
                for r in ranges:
                    if r[0] < current_max_merged[1] and r[1] > current_max_merged[0]:
                        current_max_merged[0] = min(current_max_merged[0],r[0])
                        current_max_merged[1] = max(current_max_merged[1],r[1])
                    else:
                        new_ranges.append(r)                
                new_ranges.append(current_max_merged)                                             
                ranges = new_ranges
              
        # print("#",ranges)
        # print(lastIndexOccurance)
        
        ranges.sort()
        ans = []
        for i in ranges:
            ans.append(i[1] - i[0] + 1)    

        # Time o(n ** 2) there's better way :(
        # space o(n)    
        return ans

s = Solution()
strs = "caedbdedda"
strs = "ababcbacadefegdehijhklij"
strs = "eccbbbbdec"
strs = "eaaaabaaec"
# strs = "ababcbacadefegdehijhklij"
print(s.partitionLabels(strs))