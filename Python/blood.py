class A:
    def __init__(self,bloodgroup,bloodunit):
        self.bloodgroup=bloodgroup
        self.bloodunit=bloodunit
class B:
    def __init__(self,bgn,bun):
        self.bgn=bgn
        self.bun=bun
    def meth1(self,l):
        for i in range(n):
            if l[i].bloodgroup==bgn and bun<=l[i].bloodunit:
                return True
        
        
    def meth2(self):
        k=[]
        for i in range(n):
            k.append(l[i].bloodunit)
        k.sort()
        mini=k[0]
        
        for i in range(n):
            if l[i].bloodunit==mini:
                print(l[i].bloodgroup)
            

global n
global l
global available
available=False
l=[]
n=int(input())
for i in range(n):
    bg=input()
    bu=int(input())
    o=A(bg,bu)
    l.append(o)

bgn=input()
bun=int(input())
obj=B(bgn,bun)
r=obj.meth1(l)
if r==True:
    print('Blood Available')
else:
    print('Blood not available')
obj.meth2()
    
        
