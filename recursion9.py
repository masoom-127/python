# Write a recursive function to print the cubes of the first N natural numbers. 5.
def even(n):
    if n>0:
        even(n-1)
        print(n**3)
         
        

even(3)