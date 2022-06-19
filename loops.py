#problem:1
# i=1
# while (i<51):
#     print(i)
#     i=i+1

# problem:2
# l1=[1,2,3,4,5]
# i=0
# while (i<len(l1)):
#     print(l1[i])
#     i=i+1

#problem:3
# a=int(input("Enter no. to print its table"))
# for i in range(1,11):
#     print(f"{a}*{i}={a*i}")   # f->fstring
#     i=i+1

#problem:4
# l1=["harry","sohan","sachin","rahul","viveks"]
# for i in range(0,5):
#     if("s"in l1[i]):
#         print(l1[i])
#     else:
#         continue

#problem:5
# i=1
# while(i<11):
#     print(f"{a}*{i}={a*i}")
#     i=i+1

#problem:6
# a=int(input("Enter any no."))
# if(a>1):
#     for i in range(2,int(a/2)+1):
#         if(a%i==0):
#             print("its not a prime no.")
#             break
            
#     else:
#         print("its a prime no.")
# else:
#     print("its neither prime nor composite")

#problem:7
# sum=0
# i=1
# n=int(input("Enter no. to find its sum "))
# while(i<=n):
#     sum=sum+i
#     i=i+1
# print("sum of first n natural no. is",sum)

# problem:8
# sum=1
# n=int(input("Enter no. to find its factorial"))
# for i in range(1,n+1):
#     sum=sum*i
# print("factorial of a no. is: ",sum)

#problem:9
# k=2
# for i in range(0,5,2):
#     for j in range(0,k):
#         print(end=" ")
#     k=k-1
#     for j in range(0,i+1):
#         print("*",end="")       //end=" " will give space
#     print("\r")                 // move to next line like \n but gives less space between line

#problem:10
# n=int(input("Enter any no."))
# for i in range(10,-1,-1):
#     print(n*i)

# problem:11
# n=8
# for i in range(0,8):
#     for j in range(0,8):
#         if(i==0 or i==n-1 or j==0 or j==n-1):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print("\r")




