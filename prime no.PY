i = 2
a=int(input("enter the number"))
while (i<a):
    if (a%i == 0):
        print(a, 'is not a prime number')
        break
    i = i + 1
else:
    print(a, 'is a prime number')


