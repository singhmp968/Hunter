a,b=map(int,input().split())
x=list(map(int,input().split()))
larg=0
'''if(b==1):
        larg=max(x)
elif(b==len(x)):
        larg=min(x)'''
while(b!=0):
        larg=max(x)
        x.remove(max(x))        
        b=b-1
print(larg)

        
