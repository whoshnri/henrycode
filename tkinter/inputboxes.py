from tkinter import *


root = Tk()

label = Label(root, text='Enter your name')
label.pack()

e = Entry(root , background='#2f2f2f' ,width=50 , fg='white')
e.pack()
# e.insert(0 , 'Enter your name') #rigid placeholder


def click1():
    my_label = Label(root , text=f'Your name is {e.get()}') #e.get shows the input of the Entry 'get'
    my_label.pack()
my_button = Button(root , text='click me' , padx=50 ,fg='#2f2f2f', command=click1 ,bg='white')
my_button.pack()




root.mainloop()