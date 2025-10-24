#write python code create pair player in crecket
l1=input("enter a number using ,").split(',')
i=0
set(l1)
for i in l1:
    for j in list(l1)[i::]:
        print(i,j)
         