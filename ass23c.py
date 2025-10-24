# Write a Python script to calculate sum of digits of a given number 
a=int(input("enetr an number"))
s=0
su=0
while a!=0:
    s=s+a%10 

    a=a//10 


print(s)
