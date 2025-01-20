#i built this in 4 hours 
#took so log cuz the logic was kinda confusing




print('')
player_name = input("Please Enter your name: \n")



def game():
    p = 0
    c = 0
    message = 'LETS PLAY ROCK PAPER SCISSORS'
    print(message.center(49, "-"))
    message_score = f'{player_name} : {p} - {c} : Computer'
    print(message_score.center(49, '-'))

    parse = False

    while parse == False:
        correct = False
        while correct == False:
            try:
                player_choice = input("Enter...\n1 for Rock,\n2 for Paper,\n3 for Scissors: \n ")
                player_choice = int(player_choice)
                correct = True

            except ValueError as e :
                print(e)        #this trtry except block is kinda unnecessary

            if player_choice in [1,2,3]:
                print(f'You chose: {"Rock" if player_choice== 1 else "Paper" if player_choice== 2 else "Scissors" }')

            else:
                message = "Please enter a valid number within the range"
                print(message)
                print('')
                correct = False
  

        import random
        def run_countdown():
            print("Computer loading.....")
            print()
            yield 1
            yield 2
            yield 3

        g = run_countdown()
        print(next(g))
        print(next(g))
        print(next(g))

        comp_output = random.choice([1,2,3])

        print('')
        print(f'Computer Generated: {"Rock" if comp_output == 1 else "Paper" if comp_output == 2 else "Scissors" }')


        if comp_output == player_choice:
            print("Its a tie!😒")
        if comp_output != player_choice:
            if comp_output == 1 and player_choice == 2:
                print("You win!🥳🥂")
                p += 1

            elif comp_output == 1 and player_choice == 3:
                print("Computer wins!💩")
                c += 1

            elif comp_output == 2 and player_choice == 1:
                print("Computer wins!💩")
                c += 1

            elif comp_output == 2 and player_choice == 3:
                print("You win!🥳🥂")
                p += 1
 
            elif comp_output == 3 and player_choice == 1:
                print("You win!🥳🥂")
                p += 1

            else:
                print("Computer wins!💩")
                c += 1


        replay = input(f"Do you wish to Play again, {player_name}?\n Y if yes , N if no: ")
        if replay in 'Yy':
            print('')

        else:
            print('')
            print (f"Thanks for playing {player_name} 😻\n")
            parse = True
           

    message_score = f'{player_name} : {p} - {c} : Computer'
    print(message_score.center(49, '-'))
    
    if p > c :
        message = f'{player_name} wins🥳🥂'
    elif p == c:
        message = f'Its a tie!😒'
    else:
        message = f'{player_name} lost to Computer 💩'


    line03 = message.center(50 , ' ')
    print(line03)

game()


        































