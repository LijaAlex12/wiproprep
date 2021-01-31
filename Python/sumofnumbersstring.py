import re
n=input()
# sentence = 'Extract 100 , 100.45 and 10000 from this string'
s = [float(s) for s in re.findall(r'-?\d+\.?\d*', n)]
print(int(sum(s)))
