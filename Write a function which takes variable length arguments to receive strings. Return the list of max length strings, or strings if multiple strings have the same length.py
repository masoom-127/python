def maxlenstring(*t):
    max_len=0
    l1=[]
    for s in t:
        if max_len<len(s):
          max_len=len(s)
    return [s for s in t if len(s)==max_len]

print(maxlenstring("dsn","sdlfmmsd","ksdfhsei"))
