import random
#computer generation 
comp = ""
comp_num = random.randint(1,3) 
if comp_num == 1:
    comp = "R"
elif comp_num == 2:
    comp = "P"
else:
    comp = "S"
print("Enter your pick!")
player = input("R, P, S: ")
user = player.upper()
while user != "R" and user != "P" and user != "S" :
    player = input("R, P, S: ")
#winning condition
def is_win(a , b):
    if(a == "R" and b == "S") or (a == "P" and b == "R") or (a == "S" and b == "P"):
        if a == "R" and b == "S":
            print ("Rock beats Scissors")
        if a == "P" and b == "R":
            print ("Paper beats Rock")
        if a == "S" and b == "P":
            print ("Scissors beats Paper")
        print("You win!")
    elif(b == "R" and a == "S") or (b == "P" and a == "R") or (b == "S" and a == "P"):
        if b == "R" and a == "S":
            print ("Rock beats Scissors")
        if b == "P" and a == "R":
            print ("Paper beats Rock")
        if b == "S" and a == "P":
            print ("Scissors beats Paper")
        print("Computer wins!")
    else:
        print("Its a tie!")
is_win(user , comp)

