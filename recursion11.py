# Write a recursive function to calculate the sum of digits of a given number. 
def sum(n):
    if n>0:
        s+=n%10
        print(s)
        sum(n//10)
                
sum(3234)