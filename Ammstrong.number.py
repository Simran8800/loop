n=int(input("enter the number"))
i=n
sum=0
while (n>0):
    sum=sum+(n%10)*(n%10)*(n%10)

    n=n//10
if i==sum:
    print("armstrong")
else:
    print("not a armstrong")