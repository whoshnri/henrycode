from tkinter import *
#in tkinter everything is a window
#to start we create the root window

root = Tk()

#creating a label widget

my_label1 = Label(root , text='Hello World!!!')
my_label2 = Label(root , text='My name is Henry')
my_label3 = Label(root , text='This is Tkinter')

#putting things on the screen 
#using the pack method
# my_label1.pack() #this positions all the elemets i the smallest space required as possible

##positioning with the grid system
my_label1.grid(row=0 , column=0) #all these grid formatting can also be assigned to the widget at the point of creation
my_label2.grid(row=1 , column=1)
my_label3.grid(row=2 , column=2)

root.mainloop()










