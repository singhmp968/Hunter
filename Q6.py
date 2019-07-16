x=int(input())
li=list(map(int,input().split()))[:x]
for i in range(x):
        if((i%2==0)and(li[i]%2!=0)or(i%2!=0)and(li[i]%2==0)):
                
                 print(li[i],end=" ")     
