import random

#guess the number 
#bingo
'''
def gue_ss(x):
    bingo_num = random.randint(1,x)
    print(bingo_num)
    trials = 5
    trial = 0
    guess = 0
    while int(guess) != bingo_num and trial < trials:
        guess = input(f"Enter your guess {str(trials - trial)} trial(s) left: ")
        if int(guess) < bingo_num:
            print(f"{str(guess)} is too low! Guess higher!")
        elif int(guess) > bingo_num:
            print(f"{str(guess)} is too high! Guess lower!")
        else:
            print("BINGO!")
        if trial == trials - 1:
            print("OUT OF TRIES , GAME OVER!")
        trial += 1

gue_ss(35)


def computer_guess(x):
    num = 1
    check = "a"
    i = 0
    try:
        if num == 1:
            guesses0 = random.randint(0,x)
            print(f"My guess is: {str(guesses0)}")
            check = input(f"Is {str(guesses0)} correct? < H if High, L if Low, C if Correct ")
            while check.lower() != "h" and check.lower() != "l" and check.lower() != "c":
                print("Incorrect check. Please re-check")
                check = input(f"Is {str(guesses0)} correct? < H if High, L if Low, C if Correct ")
            if check.lower() == "c" :
                print("Yay I Win!")
                i = 100
            elif  check.lower() == "l":
                print("Too low, okay ill try again")
                i = 1
                num = 2
                b = random.randint(guesses0,x)
                j = "l"
            elif check.lower() == "h":
                i = 1
                num = 2
                b = random.randint(0,guesses0) 
                j = 'h'
        if num == 2:
            guesses1 = b
            print(f"My guess is: {str(guesses1)}")
            check = input(f"Is {str(guesses1)} correct? < H if High, L if Low, C if Correct ")
            while check.lower() != "h" and check.lower() != "l" and check.lower() != "c":
                print("Incorrect check. Please re-check")
                check = input(f"Is {str(guesses1)} correct? < H if High, L if Low, C if Correct ")
            if check.lower() == "c" :
                print("Yay I Win!")
                i = 100
            elif j == 'l' and check.lower() == "l":
                print("Too low, okay ill try again")
                num += 1
                b = random.randint(guesses1 + 1,x)
                k = 'll'
            elif j == 'l' and  check.lower() == "h":
                print("Too high, okay ill try again")
                num += 1
                b = random.randint(guesses0 + 1,guesses1 - 1)
                k = 'lh'
            elif j == 'h' and check.lower() == "l":
                print("Too low, okay ill try again")
                num += 1
                b = random.randint(guesses1 + 1,guesses0 - 1)
                k = 'hl'
            elif j == "h" and check.lower() == "h":
                print("Too high, okay ill try again")
                num += 1
                b = random.randint(0,guesses1 - 1)
                k = 'hh'
            else :
                print("Incorrect check. Please re-check")
                check = input(f"Is {str(guesses1)} correct? < H if High, L if Low, C if Correct ")
        if num == 3:
            guesses2 = b
            print(f"My guess is: {str(guesses2)}")
            check = input(f"Is {str(guesses2)} correct? < H if High, L if Low, C if Correct ")
            while check.lower() != "h" and check.lower() != "l" and check.lower() != "c":
                print("Incorrect check. Please re-check")
                check = input(f"Is {str(guesses2)} correct? < H if High, L if Low, C if Correct ")
            if check.lower() == "c" :
                print("Yay I Win!")
                i = 100
            if k == "ll" and check.lower() == "l":
                print("Too low, okay ill try again")
                num += 1
                b = random.randint(guesses2 + 1,x)
                l = 'lll'
            if k == "ll" and check.lower() == "h":
                print("Too high, okay ill try again")
                num += 1
                b = random.randint(guesses1 + 1,guesses2 - 1)
                l = 'llh'
            if k == "lh" and check.lower() == "l":
                print("Too low, okay ill try again")
                num += 1
                b = random.randint(guesses2 + 1,guesses1 - 1)
                l = 'lhl'
            if k == "lh" and check.lower() == "h":
                print("Too high, okay ill try again")
                num += 1
                b = random.randint(guesses0 + 1,guesses2 - 1)
                l = 'lhh'
            if k == "hl" and check.lower() == "l":
                print("Too low, okay ill try again")
                num += 1
                b = random.randint(guesses2 + 1,guesses0 - 1)
                l = 'hll'
            if k == "hl" and check.lower() == "h":
                print("Too high, okay ill try again")
                num += 1
                b = random.randint(guesses1 + 1,guesses2 - 1)
                l = 'hlh'
            if k == "hh" and check.lower() == "l":
                print("Too low, okay ill try again")
                num += 1
                b = random.randint(guesses2 + 1,guesses1 - 1)
                l = 'hhl'
            if k == "hh" and check.lower() == "h":
                print("Too high, okay ill try again")
                num += 1
                b = random.randint(0,guesses2 - 1)
                l = 'hhh'
        if num == 4:
            print("Out of tries, You win")
            i = 100
    except :
        print("Nahh you cheated")
        '''


#### this took foreverrr ---- this was my idea of it lol
## now the best way

def guess_comp(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c" and high != low:
        if low != high:
            guess = random.randint(low,high)
            print(f"My guess is {str(guess)}")
            feedback = input("H for too high, L for too low, C for correct: ")
        else :
            guess = low #or guess = high
        if feedback.lower() == 'l':
            low = guess + 1
        elif feedback.lower() == 'h':
            high = guess - 1
        elif feedback.lower() != 'c' and feedback.lower() != 'h' and feedback.lower() != 'l':
            feedback = input("Invalid feedback, H for too high, L for too low, C for correct")
    print(f"Yayy the computer guessed correctly : {guess}")
guess_comp(1000)
