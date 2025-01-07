import random
from hangman_word import data
import string #this imports string functions 
from hangmanbody import *


def get_valid_word():
    words = random.choice(data) #random.choice pics from an list of entries
    while " " in words or "-" in words:
        words = random.choice(data)
    return words.upper()


def game():
    print("Let's Play a Game of Hangman")
    while hangman():
        pass



def hangman():
    word = get_valid_word()
    word_letters = set(word) #adds all the letters in the word chosen by the computer to a set
    isAlphabet = set(string.ascii_uppercase) #this keeps all the uppercase alphabet letters in a set called isAlphabet
    used_letters = set() # this empty set stores the lettes used by the user in guessing
    lives = 6
    score = 0


    #getting user input
    while len(word_letters) > 0 or lives > 0:
        #letting the user know what he has guessed 
        print("You have used these letters: " + " ".join(used_letters))
        print ("You have " + str(lives) + " life(s) left")

        print(hangman_drawing(6 - lives))

        #what the current word is
        word_guess = [letter if letter in used_letters else '-' for letter in word]
        word_list = [letter for letter in word]
        print("Current word: " + " ".join(word_guess))
        
        user_letter = input("Guess a letter: ").upper() #this sets the input to uppercase 
        if user_letter in isAlphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print()
            else: 
                lives = lives - 1
                print(user_letter + " is not in the word\n")
        
        elif user_letter in used_letters:
            print("You have already used that. Try another one!")

        else:
            print("This character cant be used to play")
            user_letter = input("Guess a letter: ").upper()
        if lives == 0 :
            print("Out of Lives, Try again")
            print(hangman_drawing(-1))
            print(f"The word was: {" ".join(word_list)}")
            play_again()
            return 
        if len(word_letters) == 0:
            print(f"Word Complete: {" ".join(word_list)}")
            score = score + 1
            play_again()
            return score

def play_again():
    answer = input("Do you want to play again? ")
    if answer.upper() in ['YES' , 'Y']:
        hangman()
    else: 
        pass



game()

'''
get more insights on sets in python and more complex word and letter functions
'''
    
