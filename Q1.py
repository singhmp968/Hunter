n=int(input())

li=list(map(int,input().split()))
res=[]

for i in li:
    
    
    if li.count(i)>1:
            
        res.append(i)
if (len(res)>=2):
    mas=set(res)
    print(*mas)
else:
    print('unique')
