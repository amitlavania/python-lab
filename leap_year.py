num = int(input("enter the year"))
if num%400==0:
        if num%100==0:
                if num%4==0:
                      print(num,"year is leap")
                else:
                    print(num,"year is not leap")
    
else:
    print(num,"year not leap")
