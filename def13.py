#e python function cal a and b fund bewteen prime number (tsrn)
# Function to print prime numbers between a and b (TSRN)
def printprimerange(a, b):
    for x in range(a+1, b):  # numbers between a and b
        isprime = True
        if x < 2:
            continue
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                isprime = False
                break
        if isprime:
            print(x, end=" ")

# Example call
printprimerange(3, 8)
