# Write a Python script to check whether a given number is a three-digit number or not
a=int(input("choose the option"))
match a:
    case a if a>=100 and a<999:
        print(" three digit number")
    case a:
        print(" is not three digit nuber")
print()
