def d1(f1):
    def greeting():
        print("happy new year")
    f1()
    return greeting
@d1
def fun():
    print("hello")

fun()