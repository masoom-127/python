#4. Write a recursive function to print first N odd natural numbers in reverse order.
def odd(n):
    if n>0:
        print(2*n-1)
        odd(n-1)

odd(3)
