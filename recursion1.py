def printn(n):
    if n>0:
        printn(n-1)
        print(n,end='')
        

    

printn(3)