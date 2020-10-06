class ExamRoom:

    def __init__(self, N: int):
        self.seats = []
        self.N = N
        

    def seat(self) -> int:
        if not self.seats:
            self.seats.append(0)
            return 0
        if self.seats == [0]:
            self.seats.append(self.N - 1)
            return self.N - 1
        else:
            dist = float('-inf')
            seat = 0
            n = len(self.seats)
            for i in range(1,n):
                newSeat = (self.seats[i] + self.seats[i - 1]) // 2
                newDist =  newSeat - self.seats[i - 1]
                if newDist > dist:
                    dist = newDist
                    seat = newSeat
            self.add(seat)
            return seat
    
    def add(self,seat):
        if len(self.seats) == 0:
            return [seat]
        
        if seat > self.seats[-1]:
            return self.seats.append(seat)
        
        addedFlag = False
        newSelfSeats = []
        for i in self.seats:
            if i > seat and not addedFlag:
                newSelfSeats.append(seat)
                addedFlag = True
            newSelfSeats.append(i)
        
        self.seats = newSelfSeats
        return

    def leave(self, p: int) -> None:
        self.seats.remove(p)
        


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)