x=int(input())
li=list(map(int,input().split(" ")))[:x]
for i in range(0,len(li),1):
   # m=li.index(li[i])
    if(li.count(i)==1):
        a=i
        
print(a)
