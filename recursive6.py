# Write a recursive function to print the first N even natural numbers
def even(n):
    if n>0:
        even(n-1)
        print(n*2)
        

even(3)