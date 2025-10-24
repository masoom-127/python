
#3 Write a Python script to count occurrence of spaces in a given string 
n=input("enter a string")
s=" "
cout=0
for i in n:
    if i in s:
        cout+=1
print(cout)