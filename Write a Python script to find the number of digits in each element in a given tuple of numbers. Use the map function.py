def countdigit(n):
    cout=0
    while n:
        n=n//10
        cout+=1
    return cout

l1=[2323]
x=map(countdigit,l1)
for i in x:
    print(i)