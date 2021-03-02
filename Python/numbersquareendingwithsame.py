n=int(input())
k=list(str(n))
square=n*n
ls=list(str(square))

s=''
ls
for i in range(-len(k),0):
    s=s+ls[i]
j=int(s)
if j==n:
    print('correct')
else:
    print('incorrect')
  
