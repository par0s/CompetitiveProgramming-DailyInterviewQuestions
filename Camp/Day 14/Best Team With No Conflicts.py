class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        array = []
        n = len(scores)
        for i in range(n):
            array.append((ages[i],scores[i]))

        array = sorted(array)[::-1]
        # print(array)
        dp = {}

        return self.findTeam(0,array,float('inf'),dp)

    def findTeam(self,ind,array,maxPossible,dp):
        including = 0
        excluding = 0

        state = (ind,maxPossible)
        if state in dp:
            return dp[state]

        if ind >= len(array):
            return 0

        #include it
        if array[ind][1] <= maxPossible:
            including = array[ind][1] + self.findTeam(ind + 1,array,array[ind][1],dp)

        #excluding
        excluding = self.findTeam(ind + 1,array,maxPossible,dp)

        res = max(including,excluding)
        dp[state] = res
        return res