row=0
while row<5:
    col=0
    while col<5:
        if row+col==2 or col-row==2 or row-col==2 or row+col==6:
            print("*",end="  ")
        else:
            print(end="  ")
        col=col+1
    row=row+1
    print()
            
            