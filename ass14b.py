# Write a Python script to check whether a given number is positive negative or zero 

a=int(input("choose the option"))
match a:
    case a if a>0 :
        print("  number is posrive")
    case a if a<0:
        print("  is negetive numberr")
    case a if a==0:
        print("   zero number")
print()
