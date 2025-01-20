from collections import Counter
from collections import namedtuple


#collections -- counter
a = "aaaaaabbbbbccccddd"
mycounter = Counter(a)
print(mycounter)#the counter stores the values as keys and the number of appearance as values
print(mycounter.values()) #return the value number for the appearance of each key
print(mycounter.keys()) #returns the uique keys present in the string

#finding the most common element
print(mycounter.most_common(2)) #the number represents the leaderboard...1 for most common , 2 for the two most common
#this returns a list with nested tuples in it

#coverting a string to a list with the Counter function from the collections module
print(list(mycounter.elements()))#i will confirm if this works without importing the counter function

#collections -- named tuples
points = namedtuple("points" , 'x,y')
pt = points(1,-4)
print(pt)
print(str(pt.x) + ", " +  str(pt.y))

'''
omoooorr, so basically the namedtuple can be used to create an immutable
tuple with a variable and arguments...the arguments are separated by a comma and they can be asigned when
creating a new tuple with the variable name of the namedtuple assigned to it 
'''

#