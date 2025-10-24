#"Write a Python script to add two matrices each of order 3x3. Store matrix elements in a list of lists."
print("enetr a first matirix")
matrix1=[
    [int (i) for i in input().split(',')],
    [int (i) for i in input().split(',')],
    [int (i) for i in input().split(',')]
]
print("enetr a secound matirix")
matrix2=[
    [int (i) for i in input().split(',')],
    [int (i) for i in input().split(',')],
    [int (i) for i in input().split(',')]
]
mtx=[[0,0,0],[0,0,0][0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        mtx[i][j]=matrix1[i][j]+[i][j]
        
        print([i][j],'')
    print()
print() 