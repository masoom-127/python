# 3. Write a Python function to find numbers in a given text, store numbers in a list and return list
 
def extractnumber(text):
    num=[]
    for i in text.split(' '):
       if type(i)==int or type(i)==float:
            num.append(float(i))
            print(num)
    return num

print(extractnumber("maso hu8 88") )


