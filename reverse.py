num = int(input("enter the number"))
rev=0
while num>0:
    rem= num%10
    rev = rev*10+rem
    num//=10
print("reverse number is",rev)
