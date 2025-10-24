#Write a Python script which takes a three digit number from the user and displays only its middle digit
print("enter a three digit number")
 
a=int(input())
if 100 <= a <= 999:
    print("midle  digit=",(a//10)%10)
else:
    print("plaese enter a valid number three didgt")