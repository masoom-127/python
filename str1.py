#write a python code check wherter it is alphabe or note
l1=input()
for i in l1:
    if i>='a' and i<='z' or i>='A'and i<='Z':
        pass
    else :
        print('string is at leart one charete not a alphabetes')
        break
else:
    print('stirng contain only alphabtres')
