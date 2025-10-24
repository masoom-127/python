# Write a recursive function to print first N odd natural numbers. 
def odd(n):
    if n>0:
        odd(n-1)
        print(2*n-1)

odd(6)