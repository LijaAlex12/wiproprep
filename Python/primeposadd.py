n=int(input())
s=0
a=[1,1,1,1,0,1,0,1,0,0]
k=list(str(n))
p=[int(i) for i in k]
for i in p:
    if a[i]==0:
        s=s+i
s
