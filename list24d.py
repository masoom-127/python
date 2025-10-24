# Write a Python script to sort list elements in descending order
print("enter a number seprated by comm")
l1=[int(i) for i in input().split(',')]
l1.sort(reverse=True)
print(l1)
print(type(l1))
