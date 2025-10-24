#  Write a Python script to create a list from a given list by selecting only even places elements

print("enter a number by using ,")
s1=[int (i) for i in input().split(',')]
l1=[]
for i in s1:
    if i%2==0:
        l1.append(i)
print(l1)


