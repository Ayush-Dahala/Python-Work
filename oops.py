# problem:1
# while (True):
#     class programmer:
#         company="Microsoft"
#         def __init__(self,name,position):
#             self.name=name
#             self.position=position
#         def record(self):
#             print(f"Employee name is {self.name} and position is {self.position}")
    
#     n1=input("Enter name of employee")
#     n2=input("Enter its position")
#     emp1=programmer(n1,n2)
#     emp1.record()
#     n3=input("Do you want to add more record : ")
#     if(n3=="n"):
#       break
#     else:
#         continue

# problem:2
# import math
# class mathMathetics:
#     def __init__(self,num):
#         self.num=num
#     def calculate(self):
#         print(f"Sqaure of no. is {self.num *self.num}")
#         print(f"Square roo of no. is {math.sqrt(self.num)}")
#     @staticmethod
#     def greet():
#         print("Hello world")

# num1=mathMathetics(64)
# num1.calculate()
# num1.greet()

#problem:3
# class abc:
#     a=20
# obj=abc()
# obj.a=0
# print(obj.a)
# print(abc.a)

#problem:4
# class train:
#     RunningUnder="Indian Railway"
#     def bookTicket(self):
#         print(f"Fair for your journey in {self.fare}")
#         print(f"Number of seat is {self.number}")
# customer1=train()
# customer1.fare=5000
# customer1.number=20
# customer1.bookTicket()

# problem:5
class add:
    def math(num1):
        print(num1.number)
num2=add()
num2.number=12
num2.math()

