#writr a python function  remove a dublicte in lis
def removdublicates(mylist):
    return list(set(mylist))

l1=[2,3,4,2,3,45,5]
print(removdublicates(l1))