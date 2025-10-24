#  Write a Python script to calculate the average of elements of a list
su=0
print("enter a number seprated by comm")
 
l1=[int(i) for i in input().split(',')]
su=sum(l1)
a=len(l1)
avg=su/a
print(f"{su} / {a} = {avg}")

 
