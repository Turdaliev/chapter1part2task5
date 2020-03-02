a = int(input('Class A'))
b = int(input('Class B'))
c = int(input('Class C'))
if (a%2) == 0:
  n1= int(a/2)
elif (a%2) ==1:
  n1= int(a/2) +1
if (b%2) ==0:
  n2= int(b/2)
elif (b%2) ==1:
  n2 = int(b/2) +1
if (c%2) ==0:
  n3= int(c/2)
elif (c%2) ==1:
  n3 = int(c/2) +1
print(n1+n2+n3)
