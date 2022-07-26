num=input("enter num")
i=0
sum=0
while i<len(num):
    a=int(num[i])
    b=len(num)
    c=a**b
    sum=sum+c
    i=i+1
print(sum)
if int(num)==sum:
  print("it is armstrong",sum)
else:
  print("not armstrong",sum)
