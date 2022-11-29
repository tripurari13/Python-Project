import random
print("="*184)
print("%100s"%"ROCK PAPER SCISSORS!!!")
print("="*184)
element=["Rock","Paper","Scissors"]
uscore=0
cscore=0
tscore=0
sure="y"
while sure=="y":
    cpu=element[random.randrange(0,3)]
    user=input("Enter your choice (Rock, Paper, Scissors) : ")
    print("Computer's choice:",cpu)
    if cpu=="Paper" and user=="Rock":
        print("You lose... Paper covers rock!")
        cscore+=1
    elif cpu=="Paper" and user=="Scissors":
        print("You win... Scissors cuts paper!")
        uscore+=1
    elif cpu=="Rock" and user=="Scissors":
        print("You lose... Rock smashes scissors!")
        cscore+=1
    elif cpu=="Rock" and user=="Paper":
        print("You win... Paper covers rock!")
        uscore+=1
    elif cpu=="Scissors" and user=="Rock":
        print("You win... Rock smashes scissors!")
        uscore+=1
    elif cpu=="Scissors" and user=="Paper":
        print("You lose... Scissors cuts paper!")
        cscore+=1
    elif cpu==user:
        print("Tie!!!")
        tscore+=1
    print("\n")
    print("="*184)
    sure=input("Do you want to play again? (y/n): ")
    if sure=="y" or sure=="Y":
        print("="*184)
        continue
    else:
        break
print("\n")
print("="*184)
print("%100s"%"Game score")
print("="*184)
print("%100s"%"Your score:",uscore)
print("%100s"%"Computer's score:",cscore)
print("%100s"%"Total ties:",tscore)
print()
print("="*77,"Thanks for playing this game!","="*76)
    
