#lambda functions

#first example
add10 = lambda x: x + 10
print(add10(5))

#secong example with multiple arguments

mul = lambda x,y : x * y
print(mul(16,3))

#lambda used with SORT method
points = [(-2,4), (2,4), (-2,-4), (2,-4)]

points_sort = sorted(points)
print(points)
print(points_sort) #default sorted by the first character (the first item in the tuple)

#using lambda function in a sorted command
points_resort = sorted(points, key = lambda x: x[1])
print(points_resort)
#so the above takes the lambda fuction and reassigns the sort rule so that the second index of the list, points is considered first while sprtig the list
#sorting based on the sum of each coordinate
points_resort = sorted(points, key = lambda x: x[0] + x[1])
print(points_resort)
#tweaking around with the arithma=etic operation after assiging x will also affect the result of the sorting

#using sorted to sort based on the second letter of a word
words = ["ebay", "clay" , "jake", "thank", "corn"]
print(words)
words_sort = sorted(words)
print(words_sort)

words_resort = sorted(words , key = lambda x : x[-1]) #sorts by the last character in each string 
print(words_resort)
#this worked and now i have a better idea of how it works

#map function 
#mapping helps assign the value of one list to that of another and can be edited using dynamic lambda functions

a = [1,2,3,4]
b = map(lambda i : i * i , a)
print(b) #this returns a map object
print(tuple(b)) #this converts it to a tuple

#i can also use the list comprehension to do that easily
b = [x * x for x in a]
print(b) #same result but less code to be written
#although for ego, ill use a bit of both when i have to

#filter function 
a = [1,2,3,4]
b = filter(lambda x : x%2 == 0, a)
print(list(b))

#using list comprehension 
b = [x for x  in a if x%2 == 0]
print(b)
#so i messed up the syntax a bit 
#the condition should come after stating the values

#reduce fuction
#reduces the list to a single value based on a lambda fuction
from functools import reduce

a = [1,12,31,4]
prod = reduce(lambda x,y  : x*y , a) #the reduce tool takes two functions
print(prod)

max = reduce(lambda x,y : x if x > y else y , a) #this worked surprisingly
print(max)




