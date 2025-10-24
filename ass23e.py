#Write a Python script to print the octal equivalent of a given decimal number Do not use oct method Is there anything else you need
d=int(input("enter a number"))
s=''
while d!=0:
    s=str(d%8)+s
    d=d//8

print(s)