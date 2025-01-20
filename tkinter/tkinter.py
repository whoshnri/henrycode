import tkinter as tk
#in tkinter everything is a window
#to start we create the root window

root = tk.Tk()

#creating a label widget

my_label = tk.Label(root , text='Hello World')

#putting things on the screen 
#using the pack method
my_label.pack()

