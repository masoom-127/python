#Define a Python class `Person` with instance object variables `name` and `age`. Set instance object variables in the `__init__()` method. Also, define a `show()` method to display the name and age of a person
class person:
    def __init__(self,name, age):
        self.name=name
        self.age=age
    def show(self):
        print("name:",self.name)
        print("age",self.age)

p1=person("masmad",23)
print(p1.show())