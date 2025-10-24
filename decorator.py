def d1(f1):
    def greeting():
        f1()
        print(" goof bye")
    
    return greeting
@d1
def fun():
    print("hello")

fun()