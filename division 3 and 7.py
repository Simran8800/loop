a=int(input("enter the no"))
b=int(input("enter the no"))
while a<=b:
    if a%3==0:
        print("nav")
    if a%7==0:
        print("gurukul")
    else:
        print(a)
    a=a+1