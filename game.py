i=0
num=40
while i<=3:
    a=int(input("enter the number,1 to 100"))
    if a==num:                                                                                                                                                                                                                                    
        print("wins")
        break
    elif a<=35:
        print("clouse the number")
    elif a<=45:
        print ("greater than")
    else:
        print("you loss the game")
    i=i+1

