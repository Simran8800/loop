i=0
while i<=3:
    a=int (input("enter the number"))
    if a==5:
        print("wow you guessed currect number")
    elif a>5:
        print("greater than 5")
    elif a<5:
        print("less than 5")
        # break
    else:
        print("false" )
    i=i+1