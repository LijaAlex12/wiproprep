import statistics
import math
n=int(input())
l=[]
for i in range(n):
    a=int(input())
    l.append(a)

for i in range(len(l)):
    h=[]
    for j in range(i+1):
        h.append(l[j])
    print(math.floor(statistics.median(h)))
      
'''      
4
5
15
1
3
5
10
5
4
'''
