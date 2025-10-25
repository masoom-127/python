#Define a class `Team` with an instance object variable, a list of team member names. Provide methods to input member names and display member names.

class team:
    def __init__(self):
        self.teammamenber=[]
    def input(self):
        print("enter member names sperated by comm")
        self.teammamenber=input().split(",")
    def dis(self):
        for i in self.teammamenber:
            print(i)    
t1 =team()
t1.input()
t1.dis()
