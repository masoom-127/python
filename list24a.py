# Write a Python script to calculate the sum of elements of a list."
su=0
print("enter a number seprated by comm")
a=input().split(',')
for i in a:
    l1=int(i)
    print(l1,end='')
    su+=sum(l1)

print(su)
print(type(l1))
