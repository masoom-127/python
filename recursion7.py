#Write a recursive function to print the first N even natural numbers in reverse order.
def even(n):
    if n>0:
        print(n*2)
        even(n-1)
        

even(3)