#repeated frist string of valuses to print it
l1=input().split()
j=0
for i in l1:
    if l1.index(i)!=j:
        print("first repead string is",i, "at index",j)
        break
    
    j+=1

