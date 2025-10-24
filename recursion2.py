# Write a recursive function to print first N natural numbers in reverse order. 

def rev(n):
    if n>0:
        print(n)
        rev(n-1)

rev(3)