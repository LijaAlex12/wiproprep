a=int(input())
flag=False
for i in range(2,a):
    if a%i==0:
        flag=True
        break
    
if flag==False:
    print('Not Possible')
else:

    # p=1
    j=10
    while(j>=10):
        h=j
        l=[]
        while(h!=0):
            b=h%10
            l.append(b)
            h=h//10
        # print(l)
        p=1
        for i in l:
            p=p*i
        # print(p)
        
        if p!=a:
            j=j+1
        else:
            l.sort()
            s=''
            for i in l:
                s=s+str(i)
            print(s)
            break
