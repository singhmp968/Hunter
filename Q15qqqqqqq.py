a1=int(input())
li1=list(map(int,input().split()))[:a1]
c1=max(li1)
res1=[]
for i1 in range(0,len(li1)):
    
               
    n1=li1[i1:]
    g1=max(n1)
    if(li1[i1]==g1):
        res1.append(li1[i1])
print(*res1)

print(c1)
