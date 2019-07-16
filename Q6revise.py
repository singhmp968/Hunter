x1=int(input())
li1=list(map(int,input().split()))[:x]
for i1 in range(x1):
        if((i1%2==0)and(li1[i1]%2!=0)or(i1%2!=0)and(li1[i1]%2==0)):
                
                 print(li1[i1],end=" ")     
