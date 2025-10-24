#write python code find poassible values of dice
l1=int(input("enter a number using ,"))
s1=set()
for i in range(1,7):
    for j in range(1,7):
        if i+j==l1:
            s1.add(i,j)
print(s1)
