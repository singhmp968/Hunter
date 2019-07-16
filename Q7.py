x=int(input())
li=list(map(int,input().split()))[:x]
for i in range(len(li)):
        for j in range(len(li)):
                for k in range(len(li)):
                        a=li[i]+li[j]
                        if((a==li[k]) and (i<j<k)):
                                print(li[i],li[j],li[k])
