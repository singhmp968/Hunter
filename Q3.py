x=int(input())
li=list(map(int,input().split(" ")))[:x]
res=[]
for i in range(0,len(li),1):
   # m=li.index(li[i])
    if(i==li[i]):
        a=li[i]
        res.append(a)
if(len(res)==0):
    print("-1")
else:
    print(*res,end = " ")
