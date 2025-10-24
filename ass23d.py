# Write a Python script to print binary equivalent of a given decimal number Do not use bin method
d=int(input("enter a number"))
s=''
while d!=0:
    s=str(d%2)+s
    d=d//2

print(s)