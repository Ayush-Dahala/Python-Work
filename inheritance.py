# problem:1
# class C_2dVector:
#     def __init__(self,i,j):
#         self.iAxis=i 
#         self.jAxis=j
#     def __str__(self):
#         return(f"{self.iAxis}i + {self.jAxis}j")
        
# class C_3dVector(C_2dVector):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.kAxis=k
#     def __str__(self):
#         return(f"{self.iAxis}i+{self.jAxis}j+{self.kAxis}k")

# obj1=C_2dVector(5,8)
# print(obj1)      
# obj=C_3dVector(2,3,4)
# print(obj)

#problem:2
# class Animals:
#     pass
# class Pets(Animals):
#     pass
# class Dogs(Pets):
#     @staticmethod
#     def bark():
#         print("bhow ! bhow")
        
# dog1=Dogs()
# dog1.bark()

#problem:3
# class Employee:
#     salary=50000
#     increment=1.5
#     @property
#     def SalaryAfterIncrement(self):
#         return self.salary*self.increment  #(SalaryAfterIncrement=salary*increment)-->attribute
#     @SalaryAfterIncrement.setter
#     def SalaryAfterIncrement(self,sai):
#         self.increment=sai/self.salary
        
# emp1=Employee()
# print(emp1.SalaryAfterIncrement)
# print(emp1.increment)
# emp1.SalaryAfterIncrement=55000
# print(emp1.increment)        
    
#problem:4
# class complex:
#     def __init__(self,a,b):
#         self.x=a
#         self.y=b 
#     def __add__(self,U):  #add two object
#         return f"{self.x+U.x}+{self.y+U.y}i"
#     def __mul__(self,U):
#         mulReal=self.x*U.x-self.y*U.y         # (a + ib) (c + id) = (ac - bd) + i(ad + bc).
#         mulImg=self.x*U.y+U.x*self.y
#         return f"{mulReal}+{mulImg}i"
    
# obj1=complex(2,3)
# obj2=complex(3,5)
# obj3=obj1 + obj2     #obj3.(obj1,obj2)
# obj4=obj1*obj2
# print(obj3)
# print(obj4)

# problem:5
# class vector:
#     def __init__(self,vec):
#         self.vec=vec
#     def __add__(self,vec3):
#         l1=[]
#         for i in range(len(self.vec)):
#             l1.append(self.vec[i]+vec3.vec[i])
#         return l1
#     def __mul__(self,vec3):
#         sum=0
#         for i in range(len(self.vec)):
#             sum+=self.vec[i]*vec3.vec[i]
#         return sum
# vec1=vector([2,3])
# vec2=vector([3,5])
# vec3=vec1+vec2
# vec4=vec1*vec2
# print(vec3)
# print(vec4)

#problem:6
