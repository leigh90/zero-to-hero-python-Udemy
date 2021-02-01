from math import pi
class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        volcalc = pi * (self.radius ** 2) * self.height
        print(round(volcalc,2))
        return round(volcalc,2)
    
    def surface_area(self):
        saarea = (2 * pi * self.radius * self.height) + (2 * self.height * self.radius**2)
        print(round(saarea,2))
        return round(saarea,2)


testcylinder = Cylinder(10,9)
testcylinder.volume()
testcylinder.surface_area()
