##write python function cal find greates number of three
def greater(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c
print(greater(3,45,5))