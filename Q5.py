"""x=int(input())
li=list(map(int,input().split()))[:x]
li2=[]
c=0
for i in range(0,x,1):
        
        for j in range(i+1,x,1):
                
                if(li[i]==li[j]):
                        a=li[i]
                        li2.append(a)
if(len(li2)==1):
        print("unique")
else:
        print(li2[0])"""
import sys
a1=int(input())
b1=list(map(int,input().split()))
for i in b1:
    if(b1.count(i)>1):
        print(i)
        sys.exit()
print("unique")
                
        
