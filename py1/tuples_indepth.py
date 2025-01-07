# this is an immutable list
mytuple = ("henry" , "bassey")
print(type(mytuple))
mytuple1 = "henry" , "bassey", "nya"
print(type(mytuple1))

#accessing elements of a tuple is similar to a list
print(mytuple1[1])
print(mytuple1[-1])

#iteeation over a tuple is similar to that of  a list using a for in loop
for i in mytuple1:
    print(i)

#checking to see if an item is in a tuple is also very easy to do
if "nya" in mytuple1:
    print("yes element exists")

#number of elements is also very easy just like in a list
print(len(mytuple1))

#counting the number of times an element appears in a tuples is also as easy as it is in a list
print(mytuple1.count("nya"))

#turning a tuple into a list
mylist = list(mytuple1)
print(type(mylist))

my_tuple = tuple(mylist)
print(type(my_tuple))

#slicing a tuple

my_tuple1 = my_tuple[0:3]
print(my_tuple1)

#unpacking a tuple
#this is a good way of assigning variables to immutable values 
#ill be using this method more often
mytuple2 = "max" , 15 , "New York"
name , age , city = mytuple2
print(name)

#one can also do something like this
#not really sure howto explain this tho
mytuple3 = 1,2,3,4,5,6,7
i1, *i2, i3 = mytuple3 #the star assigns the values between the first and last index to i1 and i3....making i2 a list
print(i1)
print(i2)
print(i3)
