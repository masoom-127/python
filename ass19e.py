#4 Write a Python script to print unique digits of a given integer
a=input("enter a number")
for i in a:
   if a.index(i) ==i:
      print(a,end=" ")
      i+=1
      print(i)
