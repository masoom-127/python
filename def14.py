#e python function cal first N fibonacci sereas natural number (tsrn)
def feb(n):
    a,b=0,1
    while n:
        c=a+b
        print(c,end='')
        a=b
        b=c
        n-=1
feb(10)