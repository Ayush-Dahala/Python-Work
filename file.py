#problem:1
# f1=open("poems.txt","r")
# data=f1.read()
# if("Twinkle"in data):
#     print("twinkle is present")
# else:
#     print("twinkle not present")
# print(data)
# f1.close()

#problem:2
# def game():
#     score=10
#     f1=open("Score.txt","r")
#     data=int((f1.read()))
#     if(data<score):
#         f1=open("Score.txt","w")
#         f1.write(str(score))

# game()

# problem:3
# for i in range(2,21):
#     with open(f"Table/Table of {i}.txt","w")as f1:
#         for j in range(1,11):
#             f1.write(f"{i}*{j}={i*j}")
#             if(j!=10):
#                 f1.write("\n")

#problem:4
with open("poems.txt")as f1:
    content=f1.read()
content=content.replace("donkey","######")
with open("poems.txt","w")as f1:
    f1.write(content)       