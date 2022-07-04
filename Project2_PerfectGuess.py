import random
def randomNumberGuess(n):
    while True:
        if(n>a):
            print("Decrease the number")
            n=int(input("Enter new decrease no."))
            continue
        elif(n<a):
            print("Increase the number")
            n=int(input("Enter new increase no."))
            continue
        else:
            print(f"Your Guess is right")
            print(f"Random no. is {a}")
            print(f"Your Guess is {n}")
            break


n=int(input("Enter any no."))
a=random.randint(1,100)
randomNumberGuess(n)