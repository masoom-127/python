#Write a Python script to create a list of first N prime numbers."
n=int(input("enetr a number"))
l1=[]
num=2
while n :
    for i in range(2,num):
        if num%i==0:
            break
    else:
        l1.append(num)
        n-=1
    num+=1

print(l1)
        

    
