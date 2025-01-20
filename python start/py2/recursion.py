def add_one(num):
    if num >= 9 :
        return num + 1
    total = num + 1
    print(total)
    return add_one(total)


add_one(1)#this works almost like a loop

#alternatively using a loop

def add_one_loop(x):
    while x <= 9:
        print(x)
        x += 1


add_one_loop(1)



#closure
# a closure is a fuction having access to the scope of its parent function
#i need to understand this 

def parent_function(person):
    coins = 3
    def play_game():
        nonlocal coins
        coins -= 1
        if coins > 1 : 
            print(f'{person} has {str(coins)} coins left')

        elif coins == 1:
            print(f'{person} has {str(coins)} coin left')

        else :
            print(f'{person} is out of coins')

    return play_game()

parent_function("henry")
parent_function("henry")
















