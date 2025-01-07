# a decorator is a function that takes another function, a, as an argument and extends the functionality of a without modifying a

def start_end_decorator(func):

    def wrapper(*args , **kwargs): #this is a must syntax
        print("start")
        func(*args , **kwargs) #this is the placeholder for the fuction that will be placed in this decorator
        print('end')
    return wrapper


@start_end_decorator
def printname():
    print("alex")
'''
newfunc = start_end_decorator(printname)  #assign the mini function to the decorator under a new function name
newfunc() #this is so we can reuse the mini function without calling the decorator
in this case we wont use the @start_end_decorator statement
'''
printname() #this still retains its validity

#syntax of decorators when the fuction takes arguments
@start_end_decorator
def add5(x):
    print(x + 5)


add5(2)


####get back to this
#explaining function arguments in detail





















