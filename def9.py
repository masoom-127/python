#write python function cal fuctorial of the number
def fect(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
print(fect(5))