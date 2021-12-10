n=int(input("enter the number"))
i=n
while i!=1 and i!=4:
    sum=0
    while i!=0:
       rem=int(i%10)
       sum=sum+rem*rem
       i=i//10
    i=sum
if (sum==1):
    print(n,"happy number")
else:
    print(n,"unhappy number")
