string=input()
k=int(input())
p=""
for i in string:
    p=p+chr(ord(i)+k)
print(p)
