#Write a Python script to create a list of squares of numbers of a given list

print("enter a number seprated by comm")
l1=[int(i) for i in input().split(',')]
l2=[i**2 for i in l1]
for i in l2 :
    print(i)
