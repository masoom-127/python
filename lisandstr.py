#occursece of vlues
print("hello")
l1=input().split(',')
i=0
for x in l1:
    if i==l1.index(x):
        print(x," ",l1.count(x))
    i+=1



