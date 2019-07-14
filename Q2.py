x=int(input())
li=list(map(int,input().split(" ")))[:x]
li.sort(reverse = True)
for i in range(0,len(li),1):
    print(li[i],end="")
