#  Write a recursive function to print the reverse of a given number. Is there a specific question you would like to discuss further
def rev(n):
    if n>0:
        print(n%10,end='')
        rev(n//10)
       
         
rev(3234)