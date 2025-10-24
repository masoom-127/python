#write code dict to accending order
d1={n:n**2 for n in range(1,int(input("enter a number"))+1)}
print(d1)
l1=sorted(d1,reverse=True)
print("print in accending ordr by key",l1,)
for i in d1:
    print(i,'',d1[i])