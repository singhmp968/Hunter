a=int(input())
li=list(map(int,input().split()))[:a]
c=max(li)
res=[]
for i in range(0,len(li)):
    
               
    n=li[i:]
    g=max(n)
    if(li[i]==g):
        res.append(li[i])
print(*res)

print(c)
