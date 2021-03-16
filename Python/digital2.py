n=int(input())
l=[]

for i in range(n):
    a=int(input())
    l.append(a)
    l.sort()
if len(l)<2:
    print('Invalid Input')
elif l[0]==l[-1]:
    print('Equal')
else:  
    print(l[0],l[1])
