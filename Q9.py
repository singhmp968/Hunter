x=int(input())
li=list(map(int,input().split()))
for i in range(0,x):
    for j in range(i+1,x):
        if(li[i]+li[j]==0):
            print(li[i],li[j],end=" ")
            
