#Define a class `Book` with instance object variables `booked`, `title`, and `price`. Initialize them via the `__init__()` method. Also, define a method to show book variables
class Book:
    def __init__(self,bookid,title,price):
        self.bookid=bookid
        self.title=title
        self.price=price
    def showbook(self):
        print(self.price,self.bookid,self.price)

b1=Book(1,"one day",239)
b1.showbook()
