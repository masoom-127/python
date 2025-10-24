# 5. Write a recursive function to calculate the sum of the first N prime numbers.
def primesum(n):
    for i in range(2,n):
        if n%i==0:
            return False
        return True
    
    primesum(n-1)