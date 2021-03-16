# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
dict1={}
for i in range(n):
    a=input().split()
    
    dict1[a[0]]=int(a[1])

while(True):
    try:
        k=input()
        if k in dict1:
            print(k+'='+str(dict1[k]))
        else:
            print('Not found')
    except EOFError:
        break;
