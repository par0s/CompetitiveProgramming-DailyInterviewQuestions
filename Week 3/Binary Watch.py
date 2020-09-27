class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        if num < 0 or num > 10:
            return []
        res = []
        
        hours = {}
        minutes = {}
        
        for h in range(12):
            bins = bin(h)[2:]
            hash_fn = self.hash_helper(bins)
            
            if hash_fn in hours:
                hours[hash_fn].append(h)
            else:
                hours[hash_fn] = [h]
        
        for m in range(60):
            bins = bin(m)[2:]
            hash_fn = self.hash_helper(bins)
            
            if hash_fn in minutes:
                minutes[hash_fn].append(m)
            else:
                minutes[hash_fn] = [m]
        
        res = []
        for i in range(num + 1):
            hour,minute = [],[]
            if i in hours:
                hour = hours[i]
            if num -i in minutes:
                minute = minutes[num - i]   
            
            if len(hour) > 0 and len(minute) > 0:
                curr = self.combine(hour,minute)            
                for c in curr:
                    res.append(c)
        return res
    
    def combine(self,hour,minute):
        ans = []
        for i in hour:
            for j in minute:
                ans.append(self.toStr(i,j))    
        return ans
    
    def toStr(self,hour,minute):    
        minute = str(minute) if minute > 9 else "0" + str(minute)
        return str(hour) + ":" + minute        
        
    def hash_helper(self,bins):
        one = 0
        for i in bins:
            if i == "1":
                one += 1
        return one
        
            
        
        
        