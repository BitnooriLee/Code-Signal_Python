a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

b=[]
for i in a:
    b.append(i)

for i in range(len(a)):
    for j in range(len(a)):
        print(i,j)
        b[j][len(a)-1-i] = a[i][j]

print(b)
print(a)
