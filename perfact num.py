n=int(input("enter the number"))
i=1
sum=0
while n%i==0:
    sum=sum+i
    if sum==n:
        print(sum,"perfect")
    else:
        print(sum,"unperfect")
    i=i+1



    