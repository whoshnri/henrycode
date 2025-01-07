#random module
import random

#generating a random float from 0 -- 1
a = random.random()
print(a)
#this number can be so minutely small

a = random.uniform(1,10)
print(a)
#this can help with making floats within a given range

#random integers
a = random.randint(1,23) #upper bound included
print(a)

#random integer without the upper bound
a = random.randrange(1,10)
print(a)

#the random normal variate picks a random number within the graph of a mean and normal distribution
a = random.normalvariate(2,0.5)#first parameter is the mean and the next is the normal
print(a)

#
mylist = list("Henry is the best")
a = random.randint(0 , len(mylist) - 1)
print(mylist[a])
#or
a = random.choice(mylist)
print(a)

#one can also pick more than one choice
a = random.sample(mylist, 3)
print(a)

#shuffling the list 
random.shuffle(mylist)
print(mylist)

#the tutorial explained why geerating random numbers in this manner is not fit for security operations
# observe
random.seed("first")
print(random.random())
print(random.randint(1,30))
random.seed("second")
print(random.random())
print(random.randint(1,30))


random.seed("first")
print(random.random())
print(random.randint(1,30))
random.seed("third")
print(random.random())
print(random.randint(1,30))


random.seed("second")
print(random.random())
print(random.randint(1,30))
random.seed("third")
print(random.random())
print(random.randint(1,30))
#in the output it is notices than the random operations under the same seed name (first, second and third ) all have the same random values
#this means that they can be recreated elsewhere in the code making the operation not so random
#for this reason these operations previously mentioned are called pseudo random

#generation real random values
import secrets

a = secrets.randbelow(10) #from 0 till ten -- below 10
print(a)

a = secrets.randbits(4) #this returns an integer with a max of 4 binary digits -- 15
print(a)

mylist = list("henryisachamp")
a = secrets.choice(mylist)


