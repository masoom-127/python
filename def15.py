#python function cal first factors sereas natural number (tsrn)
def factor(n):
    for i in range(1,n+1):
        if(n%i==0):
            print(i,end='')
factor(36)
