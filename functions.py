# problem:1
# def func(name):
#     print("Hello "+name)

# func("ayush")

#problem:2 (factorial using recursion)
# def recursive(n):
#     if(n==1 or n==0):
#         return 1
#     else:
#         return n*recursive(n)

# print(recursive(5))

#problem:3
# def greatest(a,b,c):
#     if(a>b and a>c):
#         print("a is greatest")
#     elif(c>a and c>b):
#         print("c is greatest")
#     else:
#         print("b is greatest")

# greatest(2,3,4)

#problem:4
# def temp_convert(temp):
#     return (temp*9/5)+32
# print(temp_convert(50))

#problem:5
# print("hello world",end=",")
# print("hello ayush")

#problem:6
# def recursive_sum(n):
#     if(n<1):
#         return n
#     else:
#         return n+recursive_sum(n-1)
# print(recursive_sum(3))

#problem:7
# def pattern(n):
#     for i in range(n,0,-1):
#         print("*"*i)
#     print("\r")

# pattern(5)

#problem:8
# def inch_cm(n):
#     return n*2.54
# print(inch_cm(5))

#problem:9
# def table(n):
#     for i in range(1,11):
#         print(n*i) 
# table(5)

#problem:10
def stripword(string,word):
    newstr=string.replace(word," ")
    return newstr.strip()    #strip remove blank spaces
print(stripword("hello ayush","hello"))