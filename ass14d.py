#ind roots of quadratic equation Match and execute appropriate code on user selection
# 4 Write a Python script to take one data from user and evaluate the type of data If the data is of string type then print Monday If the data is of float type then print Tuesday If the data is of complex type then print Wednesday If the data is of type bool then print Thursday
a=eval(input("netr a bunber"))
match a:
    case a if type(a)==int:
        print("monday")
    case a if type(a)==complex:
        print("tuesady")
    case a if type(a)==bool:
        print("thirsday")
    case a if type(a)==float:
        print("friday")
    case _:
        print("not googd")