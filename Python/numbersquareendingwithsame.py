n=int(input())
square=n*n
ls=list(square)
l=len(n)
s=''
for i in range(-l):
  s+str((square[-l]))
k=int(s)
if k==n:
  print('correct')
else:
  print('wrong')
  
