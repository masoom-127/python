##write python function cal find id prime
def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
print(isprime(3))
    
