n=int(input("enter the no"))
i=1
while n>0:
    b=1
    while b<i:
        print(' ',end=' ')
        b=b+1
    j=1
    while (j<=(n*2)-1):
        print(j,end=" ")
        j=j+1
    n=n-1
    print()
    i=i+1