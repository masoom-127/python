#Define a class `Circle` with an instance object variable `radius`. Provide `setter` and `getter` for `radius`. Also, define `getArea()` and `getCircumference()` methods
class circle:
    def __init__(self,radius):
        self.radius=radius
    def set(self):
        radius=self
    def get(self):
        return self.radius
    def getarea(self):
        return 3.14*self.radius**2
    def getcircle(self):
        return 2*3.14*self.radius

c1=circle(2)
print(c1.get())
print(c1.getarea())
        
        
    