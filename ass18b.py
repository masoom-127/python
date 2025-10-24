#2 Write a Python script to print first N even natural numbers in reverse order
a = int(input("Enter a number: "))
i = 1
while  i<a:
    if a%2==0:
        print(a)
    i+=1