#Write a Python script to create a list of first N terms of a Fibonacci series.n]
n=int(input("enter an number"))
li=[] 
a=-1
b=1
while n:
    c=a+b
    li.append(c)
    a=b
    print(a)
    b=c
    n-=1

print(li)
print()
