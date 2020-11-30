class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.arr = [""] * self.n        
        self.pointer = 0

    def insert(self, id: int, value: str) -> List[str]:
        id -= 1
        self.arr[id] = value
        
        res = []
        while(self.pointer < self.n):
            if self.arr[self.pointer] != "":
                res.append(self.arr[self.pointer])
                self.pointer += 1
            else:
                break
        
        return res
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)