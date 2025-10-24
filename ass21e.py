#5 Write a Python script to display all prime numbers within a range  # range= 15  end = 45
start=int(input("enter a num"))
end=int(input("enter a num"))
for i in range(start,end):
    for x in range(2,i):
        if (i % x==0):
            break
    else:
        print(x)
print()

