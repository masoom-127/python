# Write a Python script to calculate sum of cubes of first N natural numbers
a=int(input("enetr an number"))
s=0
for i in range(1,a+1):
    s=s+i**2

print(s)
