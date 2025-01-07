name = 'Henry'
age = 17


#checking data types
# print(type(age))

# print(type(age) == type(name))

# print(isinstance(age , int))

# print(isinstance(name , str))



### creating data with constructors
# topping = str('Pepperoni')

# print(type(topping) == str)

# print(isinstance(topping , int))

# print(isinstance(topping , str))


####concatenation

# firstname = 'Henry'
# lastname = 'Bassey'

# fullname = firstname + ' ' + lastname
# print(fullname)

# fullname += ' Nya'
# print(fullname)


########casting a number to a string

# decade = str(1980)
# print(isinstance(decade, str))
# print(decade)

# print('i like rock music from the ' + decade + 's')



# ####multiple lines
# multilines =  """
# Hey how are you
#     i was just checking in
# Whats up with you
#     Have fun
# """
# print(multilines)


#####escaping specail characters with \

# multilines = ("To Gerald\n\tHey, I\'m gonna be a little late for work today. \n\tThanks for understanding! ")

# \n --> new line
# \t --> tab



#####String methods
# word = 'CalliGraPhy'

# print(word.upper())
# print(word)
# print(word.lower())

# print(multilines.title())
# print(multilines)
# print(multilines.replace('Gerald' , 'Duke'))


# title = 'menu'.upper()
# print(title.center(18 ,'-')) #10 characters long with menu in the centre (also part of 10)


#lemme make a real nice menu with methods and modules
# import random
# list_of_costs =["$1", '$2', '$3', '$5', '$4']
# list_of_items = ["Coffee" , 'Burger',"Pizza", 'Nacho', "Taco" , "Coca-cola"]

# for i in list_of_items:
#     print(i.ljust(15 , '-') + '>' + random.choice(list_of_costs))

##### characters in a string can be gotten through indexing just like in lists
word = 'supercalifragilistisexpalidocious'
word2 ='pneumonioultramicroscopicsilivolcanoconoisis'
print(len(word2))












































