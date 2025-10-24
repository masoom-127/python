def vowelcount(s):
    COUNT=0
    for ch in s:
        if ch in "aeouiAEIOU":
            COUNT+=1
    return COUNT
    
l1=["dvndvaa","dasdnfsn"]
for m in map(vowelcount,l1):
    print(m)

