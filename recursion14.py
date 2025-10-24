# rite a recursive function to print the octal of a given decimal number. 
def bin(n):
    if n>0:
        bin(n//8)
        print(n%8,end='')

bin(33)