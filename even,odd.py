numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
even=0
odd=0
i=0
while  i<len(numbers):
    if not i%2:
        even+=1
    else:
        odd+=1
    i+=1
print(odd,":",even)



# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# even=0
# odd=0
# for i in numbers:
#     if not i%2:
#         even+=1
#     else:
#         odd+=1
# print(even)
# print(odd)