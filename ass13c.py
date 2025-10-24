#4 Write a Python script to check whether a given year is a leap year or not 
print("netr a year")
a=int(input())
if a % 100==0 and a%400==0:
    print("leap year")
elif a%4==0:
    print("leap year")
else:
    print("not leap year")
