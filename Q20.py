def ifprime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

n,m=map(int,input().split())
c=0
for i in range(n,m+1):
    bina=bin(i).count('1')
    if ifprime(bina):
        c=c+1
print(c)
