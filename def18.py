#write python code create li of prime number
def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def primelist(a,b):
    l1=[]
    for i in range(a+1,b):
        if isprime(i):
            l1.append(i)

    return l1

print(primelist(10,20))

                
        
