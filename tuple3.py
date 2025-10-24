#create tuple list print 
l1=input().split(',')
temp=[]
mylist=[]
j=0

aplpha="abcdefghijklmnopqrstuvwxyz"
l1.sort()
for i in range(0,26):
    temp.clear()
    for j in l1:
        if j.startswith(aplpha[i]):
            temp.append(j)
    if(len(temp)>0):
        mylist.append(tuple(temp))
print(mylist)



