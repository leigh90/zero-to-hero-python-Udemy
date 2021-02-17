from math import sqrt
class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        dist = sqrt( (self.coor2[0] - self.coor1[0])** 2 + (self.coor2[1] - self.coor1[1])**2 )
        print(round(dist,2))
    
    def slope(self):
        slope_calc = (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])
        print(slope_calc)

lineOne = Line((3,2),(8,10))
lineOne.distance()
lineOne.slope()