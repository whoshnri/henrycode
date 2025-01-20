class Library():
    def __init__(self, name):
        self.name = name
        self.instock = [] 
        self.borrowed = []
        self.members = []
        self.member_borrow = []
        self.genres = []
    def addbook(self,book):
        self.instock.append(book.name)
        #sort books
        if book.genre == 'Romance':
            self.genres.append(f'{book.name} : {book.genre}') 
        if book.genre == 'Sci-Fi':
            self.genres.append(f'{book.name} : {book.genre}') 
        if book.genre == 'Mystery':
            self.genres.append(f'{book.name} : {book.genre}') 
        if book.genre == 'Crime':
            self.genres.append(f'{book.name} : {book.genre}') 

        print(self.genres)

    def newmember(self , member):
        self.members.append(member.name)
        print(f'"{member.name}" is now a member')

   

class Book():

    def __init__(self,name , year , genre):
        self.name = name
        self.year = year
        self.genre = genre

    def borrowbook(self,member , Library):
        if member.name in Library.members and self.name not in Library.borrowed:
            Library.borrowed.append(self.name)
            Library.member_borrow.append(member.name)
            print(f'{member.name} borrowed {self.name} successfully')
        elif self.name in Library.borrowed:
            print('This book is not available')


class Member():
    def __init__(self , name):
        self.name = name

    def returnbook(self , Library):
        if self.name in Library.member_borrow:
            print(f'{self.name} returned borrowed book ssuccessfully')
            Library.member_borrow.remove(self.name)

lib = Library('amazon')
book1 = Book('The Hunt' , 2007 , "Sci-Fi")  

mem = Member('Henry')
lib.newmember(mem)

lib.addbook(book1)
book1.borrowbook(mem , lib)

mem.returnbook(lib)




