a=int(input("enter number"))
b=2
while b<=a//2:
    if a%b==0:
        print("not prime")
        break
    b=b+1
else:
    print("prime")