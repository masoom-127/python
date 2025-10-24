# Write a Python function to find largest sorted subsequence in a given list. Return the largest subsequence as a list. 

def f1(n):
    if n==1:
        return 1
    n+f1(n-1)
    return n

print(f1(3))


    