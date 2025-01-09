from tkinter import *
root = Tk()

#to get the button to do something
def click1():
    my_label = Label(root , text='You clicked the button')
    my_label.pack()

my_button = Button(root , text='click me' , padx=50 ,fg='white', command=click1 ,bg='#2f2f2f') #pad is padding , do not call the function with the parathesis




my_button.pack()

root.mainloop()







