class Solution:
    def openLock(self, deadends, target):        
        deadends = set(deadends)        
        root = "0000"

        if (target in deadends) or (root in deadends):
            # can't be reached or can't be started
            return -1

        visited = set()
        queue = [(root,0)]
        while(queue):
            root,steps = queue.pop(0)
            next_keys = self.nextKeys(root)
            for key in next_keys:                
                if (key not in visited) and (key not in deadends):                    
                    if key == target:
                        # print(root,key)
                        return steps + 1
                    visited.add(key)
                    queue.append((key,steps + 1))        
        return -1
    
    def nextKeys(self,key):
        arr = []
        key_l = 4
        for i in range(key_l):
            # adding one to each digit of the key
            before = key[:i]
            change = (int(key[i]) + 1) % 10
            change = str(change)            
            after =  key[i + 1:] if i < 3 else "" #index out of range marker for i = 3
            arr.append( before + change + after)     

        for i in range(key_l):
            # subtracting one to each digit of the key
            before = key[:i]
            change = int(key[i]) - 1
            if change == -1:
                change = 9
            change = str(change)           
            after =  key[i + 1:] if i < 3 else "" #index out of range marker for i = 3
            arr.append( before + change + after)    

        return arr

s = Solution()
deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
target = "8888"
deadends = ["0000"]
target = "8888"
print(s.openLock(deadends,target))
# print(s.nextKeys(target))
