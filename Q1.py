n=int(input())
res=[]

li=list(map(int,input().split(" ")))[:n]
for i in range(0,len(li),1):
    
    
    if li.count(i)>1:
            
        res.append(i)
if (len(res)>=2):
    mas=set(res)
    print(*mas)
else:
    print('unique')
