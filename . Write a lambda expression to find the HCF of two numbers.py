hcf=lambda a,b:(b if a%b==0 else hcf(a%b,b)) if a>b else (a if b%a==0 else hcf(a,b%a))
print(hcf(12,18))