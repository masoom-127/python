#write code  and add all odd of list in tuple
l1=input().split(',')
s1=tuple(l1)
s=0
for i in s1:
    if i%2==1:
        s=s+i
print(s)