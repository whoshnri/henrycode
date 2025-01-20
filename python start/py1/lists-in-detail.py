#lists in more detail 
#basic list example

my_list = ["apple", "orange" , "banana"]
#lists can contain multiple data types
my_list2 = ["apple", 12 , True]

print (my_list2[2]) #returns the 3rd index
#negative 1 (-1) indexing returns the first item of the list

print(my_list[-1])

#iterating with a for in loop
for item in my_list2:
    print(item)

my_list2.append(my_list[2])#places the item i paratheses {()} at the end of a list

#checking if an item is in a list we use the in command
if "banana" in my_list2:
    print("banana here")
else:
    print("no banana here")

#checking number of elements in a list
print(len(my_list)) #outputs three

#inserting items at a specific index
my_list2.insert(3,"Blueberry")
print(my_list2[3])

#pop() removes the last item on a list and is re-assignable
new_item = my_list2.pop()
print(my_list2)
print(f"Removed item was: {new_item}")

#removing a specific element with .remove
#since new_item is banana , i can remove banana for my_list
my_list.remove(new_item)
print(my_list) #done

#clearing a list 
my_list2.clear()
print(my_list2) #empty list

#sorting a list
my_list3 = [1,3,6,2,6,8,1,2,9,11,45,21]
my_list3.sort()
print(my_list3)

#reversing a list

my_list4 = ["apple" , "watermelon", "grapefruit", "squash" , "pineapple"]
my_list4.reverse()
print(my_list4)

#multiple lists

my_list5 = [1 ,2 ,3, 4] * 12
print(my_list5) #repeats the sequence the stateed umber of times

#concatenation of lists using the plus sign
my_list6 = my_list3 + my_list
print(my_list6)

#slicing a list .....the key is to assign it and create a start and stop index in the square brackets using a colon
#the new sliced list does not comtain the stopping index
my_list7 = [1,2,3,4,5,6,7,8,9]
my_list8 = my_list7[0:4]
my_list9 = my_list7[4:9]
print(my_list8 + my_list9)

#cloning a list
'''
foreword here is that;;;;;simply assigning a new list to an existing one isnt going to be so convenient 
cuz changing a value in one list also changes the value in the previous one
hence we can easily copy the values of an existing list to a new one using .copy()
'''
mylist = my_list7.copy()
print(mylist)

#list comprehension 
#this is a faster way of creating a new list from and existing list

mylist1 = [i*i for i in mylist] #this iterates over a list and squares the value for each tem the assigns it to the appropriate index
print(mylist1)
 
#>> this can also be done with words
mylist2 = ["appples" , "banabas" , "pineapples"]
mylist3 = [j + "blas" for j in mylist2]
print(mylist3) #works perfectly






