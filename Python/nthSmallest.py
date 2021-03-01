n=int(input())
a=[]
for i in range(n):
  a[i]=int(input())
nthsmallest=int(input())
for i in range(0,n-1):
  for j in range(i+1,n):
    if a[i]>a[j]:
      t=a[i]
      a[i]=a[j]
      a[j]=t
print(a[nthsmallest])
      
