
#remove int values from list str or send another list values
l1=[39,3.3,'abc',3+4j,True,30,40]
l2=[]
i=0
while i<len(l1):
    if type(l1(i))==int:
        l2.append(l1[i])
    i+=1
print(l2)
