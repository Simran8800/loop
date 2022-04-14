
p= input("Input your password")
x = True
while x:  
    if (len(p)<6 or len(p)>12):
        break
    elif not ("[a-z]",p):
        break
    elif not ("[0-9]",p):
        break
    elif not ("[A-Z]",p):
        break
    elif not ("[$#@]",p):
        break
    elif ("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")