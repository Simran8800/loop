i=int(input("enter the number"))
n=1
while i>0:
    n=n*i
    i=i-1
    if n>=i:
        print("factorial=",n)
    else:
        print("not a factoril")

