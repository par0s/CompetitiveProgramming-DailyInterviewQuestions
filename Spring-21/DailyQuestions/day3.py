class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.updates = []
        self.rectangle = rectangle
        

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.updates.append([row1,col1,row2,col2,newValue])
        

    def getValue(self, row: int, col: int) -> int:
        for i in range(len(self.updates) - 1,-1,-1):
            arr  = self.updates[i]
            if arr[0] <= row <= arr[2] and arr[1] <= col <= arr[3]:
                return arr[4]
        
        return self.rectangle[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)