# Write a Python script to take a string from the user If the string is a part of 'education' then print 'Two' and If the string is a part of 'services' then print 'Three'

x=input("enter a some data")
match x:
    case x if x in "my":
        print("one ")
    case x if x in "masoom":
        print("two")
    case x if x in "ali":
        print("ali raza")
    case _:
        print("not is mt famly")