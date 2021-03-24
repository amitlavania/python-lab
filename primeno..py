#program to check prime number
n=int(input("enter the number"))
i=1
c=0
while n>i:
    if n%i==0:
      c=c+1
    i=i+1
if c == 2:
    print("the number is not a prime number")
else:
    print("the number is prime")
