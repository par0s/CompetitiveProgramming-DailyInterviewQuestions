class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secretCount = {}
        n = len(secret)
        
        for i in secret:
            if i in secretCount:
                secretCount[i] += 1
            else:
                secretCount[i] = 1
                        
        bulls = 0
        cows = 0
        bullHits = [0] * n            
        
        for i in range(n):
            if secret[i] == guess[i]:
                bulls += 1
                secretCount[secret[i]] -= 1
                bullHits[i] = 1        
        
        for i in range(n):
            if not bullHits[i] and guess[i] in secretCount and secretCount[guess[i]] > 0:
                cows += 1            
                secretCount[guess[i]] -= 1        
        
        return str(bulls) + "A" + str(cows) + "B"
                
                
            
        