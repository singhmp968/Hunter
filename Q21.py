n,m= map(int,input().split())
l=[]
ind=[]
for i in range(n):
    l.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        if l[i][j] == 0:
            ind.append([i,j])
for a in ind:
    row,col=a[0],a[1]
    for i in range(n):
        for j in range(m):
            
            if i == row:
                l[i][j]=0
            if j == col:
                l[i][j] = 0
for i in l:
    print(*i,end = "\n")
