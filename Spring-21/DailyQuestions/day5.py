class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        unique = {}
        res = [0] * (k + 1)
        
        for log in logs:
            if log[0] not in unique:
                unique[log[0]] = set([log[1]])
            else:
                unique[log[0]].add(log[1])
        
        
        for u in unique:
            res[len(unique[u])] += 1
        
        return res[1:]
        