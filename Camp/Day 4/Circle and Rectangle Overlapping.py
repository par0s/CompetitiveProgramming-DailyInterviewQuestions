class Solution:
    def getDist(self,c1,c2):
        xDist = c1[0] - c2[0]
        yDist = c1[1] - c2[1]
        d = (xDist ** 2) + (yDist ** 2)
        return d ** (0.5)
    
    def checkOverlap(self, r: int, xc: int, yc: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        lb = (x1,y1)
        rt = (x2,y2)
        lt = (x1,y2)
        rb = (x2,y1)
                
        c = (xc,yc)
                
        #left and right up
        for i in range(y1,y2 + 1):
            d1 = self.getDist(c,(x1,i))
            d2 = self.getDist(c,(x2,i))
            if d1 <= r or d2 <= r:                
                return True

        for i in range(x1,x2 + 1):
            d1 = self.getDist(c,(i,y1))
            d2 = self.getDist(c,(i,y2))
            if d1 <= r or d2 <= r:                
                return True
        
        #inside check
        if x1 < xc - r and x2 > xc + r and y1 < yc - r and y2 > yc + r:           
            return True
        return False
        
      
