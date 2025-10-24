#python write code lcm (tsrs)
def lcm(a,b):
    l=a if a>b else b
    while l<=a*b:
        if l%a==0 and l%b==0:
            break
        l+=1
    return l

    
print(lcm(4,6))


