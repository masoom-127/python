#5 Write a Python script to print table of user's choice
n=int(input("enter a choice"))
for i in range(1,11):
    #print(n*i,end='')
    print("{}*{}={}".format(n,i,n*i))
