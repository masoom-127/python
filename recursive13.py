# 3. Write a recursive function to print the binary of a given decimal number.
def bin(n):
    if n>0:
        bin(n//2)
        print(n%2,end='')

bin(33)