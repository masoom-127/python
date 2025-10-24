# Write a function to check if the given sides of a triangle can form a valid triangle or not. Define a decorator to print "Right Angled Triangle" if the triangle is a right-angled triangle
def d5(f1):
    def t1(a,b,c):
       x=f1(a,b,c)
       if x:
        if a>b and a>c:
           if a**2 ==b**2+c**2:
              
              

    return t1

@d5
def istreinage(a,b,c):
    if(a+b>c and a+c>b and b+c>a):
        return True
    else:
        False