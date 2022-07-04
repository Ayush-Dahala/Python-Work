#problem:2
# name=input("Enter name")
# marks=int(input("Enter marks"))
# phoneNo=int(input("Enter Phone no."))
# print("NAme of student is {} ,his marks is {} and phone no. is {}".format(name,marks,phoneNo))

#problem:3
# l1=[str(7*i) for i in range(1,11)]
# print(l1)
# print("\n".join(l1))

#problem:4
# l1=[2,3,4,5,3,4,10,3,2,15,15]
# func=lambda a : a%5==0
# print(list(filter(func,l1)))

#problem:5
from functools import reduce
l1=[2,3,4,5,3,4,10,3,2,15,]
val=reduce(max,l1)
print(val)
