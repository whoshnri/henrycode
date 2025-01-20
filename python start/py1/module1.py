import random

def roll_dice() :
    return random.randint(1,6) 

def flip_coin():
    face = random.randint(1,2)
    if face == 1:
        return "Heads"
    else :
        return "Tails"

feet_in_km = 4450
game_skakers = ["Hudson" , "Triple G", "Babe", "Kenzy", "Double G", "Bunny" , "Ruthless"]


class Student:
    def __init__(self, name, age, departmet, gpa, average_attendance): #new syntax to learn
        self.name = name
        self.age = age
        self.department = departmet
        self.gpa = gpa
        self.average_attendance = average_attendance
    def on_honour_roll(self):
        approve = False
        if self.gpa >= 3.5:
            approve = True
            return approve
        else:
            approve = False
            return approve
 
class Quiz:
    def __init__(self , question, answer):
        self.question = question
        self.answer = answer
    
class seniorStudent(Student):
    def gets_job (self) :
        if self.gpa >= 3.5:
            print("YES")
        else : 
            print("no")
