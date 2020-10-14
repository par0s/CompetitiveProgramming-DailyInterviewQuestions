class FreqStack:
    def __init__(self):
        self.maxOccurance = 0
        self.frequencyDict = {}
        self.numberFrequencyInStack = {}

    def push(self, x: int) -> None:
        if x in self.numberFrequencyInStack:
            self.numberFrequencyInStack[x] += 1
        else:
            self.numberFrequencyInStack[x] = 1
        
        x_frequency = self.numberFrequencyInStack[x]
        
        if x_frequency in self.frequencyDict:
            self.frequencyDict[x_frequency].append(x)
        else:
            self.frequencyDict[x_frequency] = [x]
        
        self.maxOccurance = max(self.maxOccurance,x_frequency)

    def pop(self) -> int:                
        # print(self.frequencyDict[self.maxOccurance],self.maxOccurance)
        most_frequent = self.frequencyDict[self.maxOccurance].pop() 
        self.numberFrequencyInStack[most_frequent] -= 1
        
        while self.maxOccurance > 0 and len(self.frequencyDict[self.maxOccurance]) == 0:
            self.maxOccurance -= 1
                
        return most_frequent
        
        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop

