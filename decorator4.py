# Write a Python script to filter only int type values in a given list of elements. Use the filter function
def d4(f1):
    def printprime(n):
        for x in range(2,n):
            for i in range(2,x):
             if n%i==0:
                break
            else:
                print(x,end=' ')
        y=f1(n)
    return printprime

@d4
def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
        return True

if isprime(20):
    print("it is prime")
else:
    print("not prime ")