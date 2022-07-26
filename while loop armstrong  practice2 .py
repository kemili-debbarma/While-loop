a=input("enter num")
i=0
j=0
while i<len(a):
    k=int(a[i])
    l=len(a)
    m=k**l
    j=j+m
    i=i+1
print(j)
if int(a)==j:
   print("it is armstrong")
else:
  print("not armstrong")
