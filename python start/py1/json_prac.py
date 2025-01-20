#json is short for javascript object notation
#its a data format used for data exchange
#this kind of data is used in web applications

#this tutorial taught how to encode and decode json data with the python json module


#encoding -- turning a python script to json data
import json

person = {"firstname" : "Henry", "lastname" : "Bassey", "age" : 17, "married" : False, "children" : [{
            "name" : "Ade",
            "age" : 4
        }, {
            "name" : "Doreen",
            "age" : 5
        }
    ], "work" : "Data Scientist"

}

personJSON = json.dumps(person , indent=3 , sort_keys=True) #this turns the python dictionary into a json (javascript object) 
#the indent was just to add word spacing and paragraphing
#the sort_keys commad just sorts the keys of the python dictionary while converting it to a json object
#print(personJSON)


#can also dumb the data into a file
person_file = open("examples.json" , "w")
print(person_file.writable())
person_file.write("\n"  + personJSON)
person_file.close()

#this worked well


#converting back to python dictioary
personPY = json.loads(personJSON )
#print(personPY)

#working with classes
#first create a class
class User:
    def __init__(self, name , age):
        self.name = name
        self.age = age

user = User("Henry", 24)

#then create a custom encoding syntax
def encode_to_json(o):
    if isinstance (o, User): #if the parameter passed is an object of the User class
        return {'name' : o.name , "age" :o.age, o.__class__.__name__ : True} #this is how the json format will be returned
    else:
        raise TypeError(TypeError.add_note) #else this happens
#this is a very basic if else exception handlig fuction of some sorts
userJson = json.dumps(user, default=encode_to_json)

print(userJson)

#decoding back to a class object from a json object

#simply trying to convert from the json will return the closest convertible equivalent
#in this case that is a dictionary
user = json.loads(userJson)
print(user)
print(type(user))

#to convert it to a class and get full python object functionalities

def decode_to_python(d):
    if User.__name__ in d: #if the parameter passed is an object of the User class
        return User(name = d["name"], age = d["age"]) #this passes the attributes name and age as methods of the User class
#it basically just loads the new variable with attributes inside the User class
#dont get overwhelmed by this concept
    else:
        return d

user = json.loads(userJson , object_hook=decode_to_python)
print(type(user))
print(user.name)




















