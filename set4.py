l1=input("enter a number using ,").split(',')
l2=set(l1)
print(type(l2))

l2=input("enter a number using ,").split(',')
black_hat_candidates=set(l2)

l3=input("enter a number using ,").split(',')
red_shoes=set(l3)

l4=input("enter a number using ,").split(',')
both_red_shoes=set(l3)
l5=black_hat_candidates.intersection(red_shoes)
for c in l5:
    print(c)

