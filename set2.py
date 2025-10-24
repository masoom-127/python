#write python code create two set find even odd each set
l1=input("enter a number using ,").split(',')
odd=set()
even=set()

for i in set(l1):
    num=int(i)
    if num %2==0:
        even.add(num)
    else:
        odd.add(num)
print(type(odd),even)