def game(comp,user):
    if(comp==user):
        return None
    if(comp=="r"):
        if(user=="p"):
            return True
        elif(user=="s"):
            return False
    if(comp=="p"):
        if(user=="s"):
            return True
        elif(user=="r"):
            return False
    if(comp=="s"):
        if(user=="r"):
            return True
        elif(user=="p"):
            return False



import random
comp=random.randint(1,3)
if(comp==1):
    comp="r"
elif(comp==2):
    comp="p"
elif(comp==3):
    comp="s"
user=input("Choose Rock(r),Paper(p),Scissor(s)")
result=game(comp,user)
print("Computer choose",comp)
print("User choose",user)
if(result==True):
    print("You Win")
elif(result==None):
    print("Tie")

else:
    print("You lose")
