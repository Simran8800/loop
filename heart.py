row=0
while row<6:
    colum=0
    while colum<7:
        if (row==0 and colum%3!=0) or (row==1 and colum%3==0) or (row-colum==2) or (row+colum==8):
            print("*",end=' ')
        else:
            print(end=" ")
        colum=colum+1
    print()
    row=row+1
                
