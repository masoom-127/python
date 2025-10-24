#Write a Python script to count words in a given string."
l1=input()
l1.strip()
s1=l1.split('')
print('')
wordcount=0
i=0
while i<len(l1):
    if l1[i]!='':
        wordcount+=1
    i+=1
    print('total world:',wordcount)