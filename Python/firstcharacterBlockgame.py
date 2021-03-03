ch=input()
# ord takes any ch and gives unicode such as ascii
if(ord(ch[0])>=65 and ord(ch[0])<=90):
  print('UPPER ALPHABET')
elif(ord(ch[0])>=97 and ord(ch[0])<=120):
  print('LOWER ALPHABET')
elif(ord(ch[0])>=48 and ord(ch[0])<=57):
  print('NUMBER')
else:
  print('symbol')
