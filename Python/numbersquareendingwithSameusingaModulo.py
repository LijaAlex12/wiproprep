def fn(n):
    sq=n*n
    while n>0:
        if(sq%10!=n%10):
            return False
        sq=sq//10
        n=n//10
    return True
            

n= int(input())
if n>0:
    if (fn(n)==True):
        print('correct number')
    else:
        print('incorrect number')
else:
    print('wrong input')
