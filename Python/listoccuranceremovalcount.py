n=int(input())
p=list(str(n))
p=[int(i) for i in p]
k=int(input('digit'))
while(k in p):
    p.remove(k)
print(len(p))
