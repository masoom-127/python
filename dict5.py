l1=[input("enter a city names").split(',')]
d={}
print(type(l1))
for i in "abcdefghijklmnopqurstuvwxyz":
    name=[]
    for city in l1:
        if l1.startswith(i):
            name.append(city)
    if len(name)>0:
        d[i]=name
for k,v in d.items():
    print(k,v)