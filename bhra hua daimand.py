k=1
i=1
while i<=5:
    j=1
    while j<=5-i:
        print(" ",end=" ")
        j+=1
    b=1
    while b<=k:
        print("*",end=" ")
        b+=1
    k+=2
    print()
    i+=1
i=5
k=7
while i>0:
    j=0
    while j<=5-i:
        print(" ",end=" ")
        j+=1
    b=1
    while b<=k:
        print("*",end=" ")
        b+=1
    k-=2
    print()
    i-=1
              


