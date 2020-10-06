class MyCalendarTwo:

    def __init__(self):
        self.first = set()
        self.second = set()

    def book(self, start: int, end: int) -> bool:
        current_interval = (start,end)        
        for second in self.second:
            if self.demorganIntersect(second,current_interval):
                return False
                
        for first in self.first:
            if self.demorganIntersect(first,current_interval):
                self.second.add((max(first[0],start),min(first[1],end)))
        
        self.first.add(current_interval)        
        return True
                        
    def demorganIntersect(self,first,second):
        return (first[0] < second[1] and first[1] > second[0])


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)