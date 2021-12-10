a=int(input("enter the no"))
i=1
count=0
while i<=100: 
    if a%i==0:
        count=count+1
    i=i+1
    if count==2:
        print("prime number")
    else:
        print("not a prime number")
      
            