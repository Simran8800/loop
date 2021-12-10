ow=0
while row<7:
    col=0
    while col<7:
        if row+col==2 or col-row==2 or row-col==2 or row+col==10:
            print("*",end="  ")
        else:
            print(end="  ")
        col=col+1
    row=row+1
    print()
            
