# Write a Python script to print greater among three numbers Print number only once even if the numbers are the same
a,b,c=int(input()),int(input()),int(input())
if a>b:
    print(a if a>c else c)
else:
    print(b if b>c else c)