#this tutorial was basically a review of different errors and exceptions
#there are many errors and exceptions which can be defined from the console
#syntax errors occurs when the code structure is inaccurate
#and other errors are logical

#raising an exception
#this returns an error when a condition is met 
x = 6
if x < 5 :
    raise Exception("X fulfils the error demands")
else :
    print(x)
    #the above is more or less a way of defining your own exceptions and the case demands

#assert statements
#this raises an assertion error if the statement after the assert keyword returns as false
x = 6 
assert (x > 5), "x fulfils the error demands"

#try except 
#this tries a block of code and gives an error output if an error occurs without breaking the code flow

#with try except
try:
    x = 5
    y = 0
    print(x / y)
except ZeroDivisionError:
    print("cannot divide by 0")
print("flow was not stopped")

#without try except
'''
x = 5
y = 0
print(x / y)

print('code was not stopped') #this wont be outputted because the flow of the program was stopped due to the error
'''

#there is a way to assign an error message so you can easily print ot out

try:
    x = 5
    y = 0
    print(x / y)
except ZeroDivisionError as i: #just assign the error to a variable
    print(i) #then prit the variable
print("flow was not stopped")


















