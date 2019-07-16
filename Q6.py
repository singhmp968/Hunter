x=int(input())
li=list(map(int,input().split()))[:x]
for i in range(1,x,1):
        if(i%2==0 and li[i]!=0 or i%2!=0 and li[i]%2==0):
                print(li[i],end=" ")
                
