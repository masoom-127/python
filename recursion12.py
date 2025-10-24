# Write a recursive function to calculate the factorial of a given number.
def cal(n):
    if n==0:
        return 1
    return n*cal(n-1)

print(cal(4))   