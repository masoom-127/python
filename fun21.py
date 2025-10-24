# Write a Python function to remove duplicate elements from a given list.

def remove(mylist):
    l=set(mylist)
    return list(l)

l1=[22,33,44,33,22,33]
print(remove(l1))


