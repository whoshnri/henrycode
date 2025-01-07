#before now i never know strings can be called with single quotes in python

mystring = "hello world"
print(mystring)

# accessing characters in a string
char0 = mystring[0]
print(char0)

#slicing a string
str0 = mystring[0:5]
print(str0)

#checking whether a strig starts with or ends with a particular word or character or set of characters
print(mystring.startswith("hel"))
print(mystring.endswith("world"))

#to find the index of substrings or characters
#this returns the first index the substring or character is found at
print(mystring.find("e"))

#to replace substrings in a string
print(mystring.replace("world", "universe"))

#converting a multiworld string to a list
mystring1 = "Hello there how are you doing"
mylist = mystring1.split(" ")#the value in paratheses dictates how the items will be split
print(mylist) 
#splitting with a letter (x)
mystring1 = "Helloxtherexhowxarexyouxdoing"
mylist = mystring1.split("x")
print(mylist)

#converting a list to a string
mystring2 = " ".join(mylist)
print(mystring2)

#formatting strings
#f strings
name = "Tommy"
cgpa = 3.67
mystr = f"Hello {name}, your CGPA is {cgpa}"
print(mystr)

#

















































