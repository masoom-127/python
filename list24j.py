#Write a Python script to create two lists from a given list of numbers in such a way that the first list can have only positive numbers and the second list can have only non positive numbers."
l1=[int (i) for i in input().split(',')]
print(l1)
l2=[]
l3=[]
for i in l1:
    if i>0:
        l2.append(i)
    else:
        l3.append(i)

print(l2,'')
print(l3,'')