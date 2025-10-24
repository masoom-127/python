#  Write a recursive function to print the squares of the first N natural numbers
def even(n):
    if n>0:
        even(n-1)
        print(n**2)
         
        

even(3)