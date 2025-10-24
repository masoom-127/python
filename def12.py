##write python function cal first next prime natural number (tsrn)
import def11

def nextprime(num):
    num += 1
    while not def11.printprime(num):  # keep searching until prime found
        num += 1 
    return num

def printf(n):
    x = 2
    for i in range(1, n+1):
        print(x, end=' ')
        x = nextprime(x)

printf(10)
