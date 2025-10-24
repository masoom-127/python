def d1(h1):
    def dec(a,b):
       x= h1(a,b)
       if (x==1):
           print("coprime number")
        else:
           print("not coprime number")
           return x
    return dec

@d1
def hcf(a,b):
    h=a if a<b else b
    while h>=1:
        if a%h==0 and b%h==0:
            return h
    return h  
print(hcf(6,8))
