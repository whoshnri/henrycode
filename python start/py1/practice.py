from math import *    #importing complex math fuctions
import module1 #importing the file from the same directory
# this is my first python program
# have to admit that its a bit easier here and makes me look smarter lol

#variables
char_name = "Henry" #clearly mo need for specifying the datatype which is cool
age = "23"
print("There once was a man named " + char_name + ", and he loved being " + age + " years old")

print ("Data is ... \nlife")
phrase = "Henry and Adeshayo"
phrase0 = " are meant to be"
print(phrase + phrase0)
print(phrase.upper()) #this returns all s uppercase // .lower() for lowercase

# phrase.isupper / phrase.islower() is used to give a boolean value depending on the case nature of the string
print(len(phrase)) #checks the length of chaacters in the string, spaces included
print(len(phrase + phrase0)) 

#checking for specific characters in the string
print("\"" + phrase[0] + "\"" + " and " + "\"" + phrase[10] + "\"") #this prints out the character represeted by the index and encloses it with quotations

# to get where a character or string is we use the index function
print(phrase.index("e")) #returns accurately
# this is also kinda cool tho
print(phrase.replace("Adeshayo" , "Doreen")) #cool shiiiiii

#working with numbers
print (4+4) #pretty basic-- using the print to calculate directly 
print ((59 + (5%4)) / (30))

#storing nnumbers in variables and calculations in variables

my_num1 = 23
my_num2 = 223
sub_tract = my_num2 - my_num1
print (sub_tract)

# a better calculator
''' #hidden
def calc():
    input1 = float(input("Enter first number: "))
    si_gn = input("Enter operator(+,-,/,*): ")
    input2 = float(input("Enter second number: "))
    if si_gn == "+":
        result = input1 + input2
        print (result)
    elif si_gn == "-":
        result = input1 - input2
        print (result)
    elif si_gn == "*":
        result = input1 * input2
        print (result)
    elif si_gn == "/":
        result = input1 / input2
        print (result)
    else:
        print("Invalid Operator")


calc()
'''
#converting numbers into strings
print(str(my_num1)) # this is important for priting numbers with strings

#math fuctions
my_num3 = -34
print (abs(my_num3)) #absolute value
print(pow(my_num1 , 2)) #power of a number
print(max (my_num1 , my_num2)) #finds the larger number from a set
print(min(my_num1 , my_num2)) #finds the smaller from a set of values

print(round(3.5)) #rounds a number accordingly
print(floor(3.5)) #always rounds down
print(ceil(3.1)) #always rounds up

### getting input from the user....yayyy! - i always love stuff like this

''' #hidden
name = input("Enter your name: " ) # its so nice how you can assign inputs to variables directly in python as opposed to c++
age = input("Enter your age: " )
print ("Good to meet you, " + name + ". You are " + age  + " years old") #wow wow wow (its way more easy to use than most ill be honest)
num1 = input("Enter a number: ")
num2 = input("Enter second number: ")
ma_th = float(num1) + float(num2)
print (str(num1) + " + " + str(num2) + " = " + str(ma_th))
'''

##lists (array)
tools = ["hammer", "wrench" , "screwdriver" , "crowbar", "band saw", "air-pumps"]
print(tools[2]) # returns screwdriver

#in python you can specify a range
print(tools[1:3]) # returns a list with items of index position 1 and 2 
tools[3] = "Wires"
print(tools) # the value at index 3 is updated

### list fuctions
lucky_nums = [2, 4, 17, 20, 13, 44]
na_mes = ["rwand", "nicole", "bosh", "grafte", "numul"]

# extend a list
lucky_nums.extend(na_mes)
print(lucky_nums) # the luckynums list becomes larger because it is concactenated with the names list

#appending values to the end of a list
na_mes.append("Henry")
print (na_mes)

#inserting elements into a preffered index of the list
na_mes.insert(2, "Adeshayo") # 2 is the index where "Adeshayo will be inserted"
print(na_mes)

# .remove and .clear are used to remove specified items or clear (reset) a list

# .pop lifts an item off the end of a list
even = [2,4,6,8,10,12,14] 
odd = [1,3,5,7,9,11,13]
nu_m = even.pop()
print(even)
odd.append(nu_m) # adds the value of nu_m as the last element on the list
print(odd)

#checking if a value is in a list
print(even.index(8)) # returns 3 because thats the position of 8 in the list
print(lucky_nums.count("Henr")) # counts how many times a specified value occurs in a list

#sorting in alphabetical order
list1 = ['a','b','c','d','e','f','g','h','i','j']
list1.reverse()
print(list1) # the list is reversed in order
list1.sort()
print(list1) #list is back in alphabetical order

#copying a list
alpha_b = list1.copy()
print(alpha_b)

#tuples
# kinda like lists but the contents go in paratheses not square brackets
#tuples are immutable and cant be changed
coordinates = (2 , 4)
print(coordinates[1])

#function # 
def say_hi(name) :
    print("hello " + name)

say_hi("Henry") #calling the function --the stuff in the brackets is a parameter (duhh)
say_hi("ade")

#returning info from the function
#this enables the returned value to be reused by the rest of the code
def cu_be (num) :
    result = num * num * num
    return "The cube is " + str(result)
print(cu_be(3)) #works well but almost gave me a headache

#if statements
is_male = True
is_tall = False
if is_male and is_tall:
    print("you are a tall male")
elif is_male and not is_tall :
    print("you are a short male")
elif not is_male and is_tall :
    print ("you are a tall female") 
else :
    print("you are a short female")
#this was fun to do but the diference in syntax from javascript and c++ is very evident
# the and keyword is just "and" as opposed to "&&" and or is "or" as opposed to "||"

#deriving hte biggest number from a list of numbers
def max_min(n1 , n2 , n3 ):
    if n1 >= n2 and n1 >= n3:
        max = n1
        return  "max is " + str(max)
    elif n2 >= n1 and n2 >= n3:
        max = n2
        return  "max is " + str(max)
    else:
        max = n3
        return  "max is " + str(max)
print(max_min(1,7,5)) #mistakenly omitted the print()----- dont do that again

#password checker 
''' #hidden
def log_in(username,password):
    username1 = input("Enter username: ")
    if username1 != username:
        print("Invalid username for this session!")
    else:
        password1 = input("Enter Password: ")
        if password1 != password :
            print("Invalid Password!")
        else: 
            print("Login successful! \n Welcome back, " + username1)
    
log_in("adeshayo123","as5XIUdc") #way easier to do in python
'''

#dictionary (kinda)
d_month = {
    1 : "January",
    2 : "February",
    3 : "March",
    4 : "April",
    5 : "May",
    6 : "June",
    7 : "July",
    8 : "August",
    9 : "September",
    10 : "October",
    11 : "November",
    12 : "December" #got really tired of typing this
}
print(d_month[1]) #method one
print(d_month.get("Jan","Invalid")) #the value after the comma is a default value in case of any error

#loops
#while loop
i = 1
''' #hidden
sym_b = input("Enter symbol: ")
while i <= 20:
    if i % 2 == 0:
     print(sym_b * i)
    else:
        print((sym_b + " ") * ceil(i/2))
    i += 1
print("Done") #finally worked---created the pattern i wanted
'''

while i <= 20:
    print((" " * (i - 1)) + str(i))
    i += 1
j = 20
while j >= 1:
    print((" " * (j - 1)) + str(j))
    j -= 1 #interesting shit

#guessing game
 #hidden
''' #hidden
def guessing_game(wo_rd):
    guess_count = 1
    guess_limit = 3
    out_of_guesses = False
    gue_ss = input("Enter your guess: ")
    while gue_ss != wo_rd and not out_of_guesses :
        if guess_count < guess_limit : 
            gue_ss = input("Wrong guess, retry<" + str(guess_limit - guess_count) + " more>: ")
            guess_count += 1
        else:
            out_of_guesses = True
    if out_of_guesses:
        print("You lose!")
    else:
        print("You Win!")

guessing_game("howdy") #this works but kinda seems too easy
'''

print()

#for loops -- basic
for letter in "Henry Bassey" :
    print(letter)
#for loop -- lists
print()
friends = ["Adeshayo", "Doreen" , "Muiz" , "David", "Marella"]
for friend in friends:
    print(friend) #cool

print()

#for loop -- range of numbers
for index in range(10): # you can give a range of values (3 , 10)
    print("Today is a happy day " + str(index + 1)) ##okay

print()

for index2 in range(len(friends)):
    print(friends[index2])

''' notes on python
    it is important to to notice and memorise the difference in syntax....i feel like the 
    overall ease with python is remarkable
'''

#exponent function
print()
def exp_funct(digit, power):
    result = 1
    for count in range(power):
       result = digit * result
    print("Result is: " + str(result))
exp_funct(3 , 4) #wow......my brain was so confused here lol -- so basically use pseudo code to break steps down

# 2D lists 
number_grid = [
    [1,2,3], 
    [4,5,6],
    [7,8,9],
    [0]
] #similar tp javascript
print(number_grid[2][1]) #accessing is similar to javascript

#nested for loops
#used to parse through a 2D list

for row in number_grid:
    for cols in row:
        print(cols) #perfect


#translator
#jungle language
#all vowels become numbers and consonants gets "a" added to them

'''word_dict = input("Enter word to translate: ")
traslation = ""
for letter in word_dict:
    if letter == "a" or letter == "A" :
        letter = "1"
        traslation = traslation + letter
    elif letter == "e" or letter == "E" :
        letter = "2"
        traslation = traslation + letter
    elif letter == "i" or letter == "I":
        letter = "3"
        traslation = traslation + letter
    elif letter == "o" or letter == "O":
        letter = "4"
        traslation = traslation + letter
    elif letter == "u" or letter == "U" :
        letter = "5"
        traslation = traslation + letter
    elif letter == "k" or letter == "K":
        letter = "ke"
        traslation = traslation + letter
    elif letter == " " :
        letter = " "
        traslation = traslation + letter
    elif letter != "a" or letter != "e" or letter != "i" or letter != "o" or letter != "u" or letter != "k" :
        letter = letter + "a"
        traslation = traslation + letter
   
print(traslation) #this required a few tweaks but it went well
'''

#catching errors with try-except commands
'''
try:
    number = int(input("input a number: "))
    number2 = int(input("input a number: "))
    number = number / number2
except ValueError: 
    print("Invalid Inputs") #this catches errors under the class
except ZeroDivisionError :
    print("Cannot Divide by Zero") #there are lots of errors we can specify
'''
'''
this is good for preventing errors
-- error names can be found in the console 
'''

#reading external files in python
#kinda excited about this
try:
    file_names = open("names.txt" ,"r") #the first parameter is the files path to file 
    #the second is the permission you want to give python over the file
    print(file_names.readable()) #to check whether the file is readable -- returns true 
    # print(file_names.read()) #reads the whole file
    # print(file_names.readlines()) # this reads the files and sorts it into a list (array)
    # print(file_names.readlines()[1]) #you can specify the particular line with list indexing []

    #looping through a file with a for loop
    for line in file_names.readlines():
        print(line)
    #line represents the value of each index of the .readlines() file

    file_names.close() #generally make sure to close the file
except FileNotFoundError :
    print("File not found")

'''# appending to files -- adding stuff to the end of the file 
file_names2 = open("names.txt" ,"a") 
print(file_names2.writable())
file_names2.write("\nMa ha zalahh dhdhd")
file_names2.close()
'''

#over writing a file
try: 
    file_names3 = open("names.txt" ,"w")  #file gets created
    print(file_names3.writable())
    file_names3.write("\nMa ha zalahh dhdhd")
    file_names3.close()
except FileNotFoundError :
    print("File not found")

#creating a new file
#new files can be created just by the same syntax as writing a file and asigning a unique name to it
new_file = open("new-file.html" , "w")
print(new_file.writable())
new_file.close()
# so yeah

'''modules and pips
python file that is imported into another file
 helps in breaking down the workflow and making it easier
this is so awesome
so i created a modules.py file with a bunch of useful functions and variables to test this out
first import from external python file at the top of page '''

print(module1.flip_coin()) #this works well
#bulk python modules available at the python website
#you can also get 3rd party python modules to help get work done faster

# classes and objects
#this is used to represent complex data types 
#classes are the custom data type and an object is the representation of the class
#the syntax for creatig the  class , "student" is in my module file

student1 = module1.Student("Henry" , "17" , "Computer science" , 3.46 , True)
#instead of specifying the module, i could just use "from module1 import Student"
print(student1.name)# works
student2 = module1.Student("Adeshayo", 16 , "Agricultural Extension" , 4.4 , False)
print(student2.gpa)

'''# buildig a multiple choice quiz
quiz_prompts = [
    "What colour are bananas? \n a. Black \n b. White \n c. Yellow",
    "What colour are coconuts? \n a. Blue \n b. Brown \n c. Orange",
    "What colour are Strawberries? \n a. Red \n b. Blue \n c. Green",
    "What colour is not in a rainbow? \n a. Black \n b. Violet \n c. Yellow",
    "How many colours do rainbows have? \n a. 5 \n b. 6 \n c. 7"

]
score = 0
quiz = [
    module1.Quiz(quiz_prompts[0], "c"),
    module1.Quiz(quiz_prompts[1], "b"),
    module1.Quiz(quiz_prompts[2], "a"),
    module1.Quiz(quiz_prompts[3], "a"),
    module1.Quiz(quiz_prompts[4], "c")
]

print("HENRY TRIVIA!! \nReady to Play? \nEnter any key to continue")
key_start_game = input("")

if key_start_game != "@" :
    for p_ick in quiz:
        print(p_ick.question)
        answer = input("Enter answer (a/b/c): ")
        if answer == p_ick.answer:
            score += 1
    if score == 0 or score == 1 or score == 2 :
        print("Final Score Is: " + str(score) + ". Do better next time")
    elif score == 3 or score == 4:
        print("Good job. Final score is: " + str(score))
    else:
        print("Perfect Score of 5")
'''

#object functions
# i created the on_honour_roll function in module1.py and i can call the class function on this page
print(student1.on_honour_roll()) #this works -- returns values based on the gpa of student1 object initially declared

#inheritance
# i dint quite get this on in c++
# so basically one can make a certain class inherit all the features of another class
# the syntax is 
#this will reflect in the module1.py file
senior1 = module1.seniorStudent("Henry2", 23, "Computer Science", 3.1 , False)
print(senior1.gpa)
senior1.gets_job()
#do more study on inheritance


















