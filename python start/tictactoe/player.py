from game import *
from random import random

def choice():
    global comp_letter
    global player_letter

    x = random.choice([1,2])

    if x == 1:
        comp_letter = 'X'
        player_letter = 'O'
    else:
        comp_letter = 'O'
        player_letter = 'X'




class Game():
    def __init__(self):
        self.start_board = board
        print(self.start_board)

        self.empty = ['a', 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i']

        self.moves_comp = []
        self.moves_human = []

    def board_progress(self):
        board_play.replace((moves for moves in self.moves_comp) , comp_letter)





class Computer():
    def __init__(self):
        self.letter = comp_letter

    def start():

        #chooses where to play and makes according changes
        position = random.choice(Game.empty)
        Game.empty.remove(position)
        Game.filled.append(position)



        

