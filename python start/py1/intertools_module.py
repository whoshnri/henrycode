from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import accumulate
from itertools import groupby , count, cycle


#product
listA = [1,2,3]
listB = [4,5,6]

prod = product(listA,listB) #creates tuples of the products of each value of a with each value of b (cartesian product)
print(list(prod)) 

#permutations
#permutation of a list returns all the number of ways the contents of the list can be combined as tuples

listC = ['a', 'b' , 'c']
perm = permutations(listC)
print(list(perm))

perm2 = permutations(listC, 2) #this is like saying len(listC)permutation 2 (LP2)

#combinations
#similar to permutations just that (a,b) == (b,a) -> no repetitions
listD = [1,2,3,4]
comb = combinations(listD,2) #len(listD)Combination 2  --> LC2
print(list(comb))

#accumulate
#this returns a list of additions at any given range from 0
a = [1,2,3,4]
acc = accumulate(a)
print(a)
print(list(acc)) #returns a new list of each addition from index 0

#group by function
#itertools --> groupby
def smallerthan3(x):
    return x>3
#the function above sets the rules that will govern the grouping
a = [1,2,3,4,5,6,7,8,9] #this list to be grouped
group_obj = groupby(a , key=smallerthan3) #the first parameter is the list to be grouped and the next is the grouping function 
for key, value in group_obj:
    print(key, list(value)) #this returns each value with the list it coordiates to
#in this scenario the key for each list is a boolean that is returned from the function above

#example two, just to clarify
def isEven(x):
    return x < 5

group_obj = groupby(a , key=isEven)
for key,value in group_obj:
    print(key, list(value))


#

glossary = [{"name" : "Henry" , "age" : 23},{"name" : "Harry" , "age" : 22},{"name" : "Terry" , "age" : 23}, {"name" : "Jerry" , "age" : 21}]
def same_age(i):
    return  i['age'] == 23
group_obj = groupby(glossary , key=same_age)
for key,value in group_obj:
    print(key, list(value))


## so this long into my python journey i realised that you can simply break out of a look using the break command
#like bro wtf

for i in count(0):
    print(i)
    if i == 435:
        break

#Cycle itertool
'''
a = [1,2,4,5,3]
for i in cycle(a):
   print(i)
'''






















