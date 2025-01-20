#advanced fuctions in python

#lets say you wanna add a lot of parameters to a function
#you can do this with with args and kwarks

def food (*args , **kwargs): #the kwargs works as a dictionary of keywords and can be assecced through keys just like a dictionary or a list....a list more precisely

    for arg in args:
        print(arg)
    for key in kwargs:
        print("keyword" , kwargs[key])


food(1,2,3,banana = 1 , plantain = 2) #here the keyword is the name of the variable that would have been passed jf


#unpacking a list into a variable
#the length of the container should be equal to the number of arguments in the parameter field of a function

def nums (a , b ,  c):
    print(a , b , c)

my_list = ["yay" , 'bane' , "kayay"]
nums(*my_list)














