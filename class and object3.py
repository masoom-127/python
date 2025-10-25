# Define a class `Rectangle` with `length` and `breadth` as instance object variables. Provide `setDimensions()`, `showDimensions()`, and `getArea()` methods in it.
class rectangle:
    def __init__(self,len,breaths):
        self.len=len
        self.breadths=breaths
    def setdata(sefl,l,b):
        sefl.len=l
        sefl.breadths=b
    def show(self):
        print("lenths= ",self.len,"breadths=",self.breadths)
    def getarea(self):
        return len*self.breadths

r1=rectangle(3,4)
print(r1.show()) 
r1.setdata(6,7)
print(r1.show())    
