batches={
    'sa':200,
    'sb':300,
    'sd':240,
    'se':120, 
}
max=0
batches_code=''
for b,s in batches.items():
    if(s>max):
        max=s
        batches_code=b
print("max size batche code is",batches_code)
