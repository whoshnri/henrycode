## lemme practice more --inheritance, word functions sets and letter operations

class Human:
    def __init__ (self, name , height , age):
        self.name = name 
        self.height = height
        self.age = age
    def talk(self,lang):
        print(f"I can talk in {lang}")

class Male(Human):
    def work(self):
        print("Men do more labourious work")

male1 = Male("Henry",6,17 )
print(male1.talk("spanish"))
print(male1.work())
print(male1.age)



