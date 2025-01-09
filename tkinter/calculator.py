from tkinter import *

root = Tk()

root.title("Simple Calculator")

e = Entry(root , width=35 , borderwidth=5)

e.grid(row=0 , column=0 , columnspan=3, padx=10, pady=20 , rowspan=2)

vals = []
ans = [0]


def click(num):
    current = 0

    if isinstance(num , int) and e.get() != '+' : 
        if e.get() != str(ans[-1]):
            current = e.get()
            clear()
            e.insert(0 , (str(current) + str(num)))

        else:
            clear()
            e.insert(0, '+')
            print('"+" added automatically')

    elif isinstance(num , int) and e.get() == '+' :
        clear()
        e.insert(0 , num)

    else:
        pass

        
def add(ls = ans):
    num = int(e.get())
    if ls[-1] != num:
        vals.append(int(e.get()))
        print(vals)
        clear()
        e.insert(0 , '+')
    elif ls[-1] == num:
        clear()
        e.insert(0 , '+')
        




def clear():
    e.delete(0 , END)


def clear_all():
    clear()
    vals.clear()
    ans.clear()
    ans.append(0)
    print(vals)


def calc():
    vals.append(int(e.get()))
    print(vals)
    result = 0
    if len(vals) > 1:
        for val in vals:
            result = (result + val)
        clear()
        e.insert(0 ,result)
        ans.append(result)
        print(ans)
    else:
        clear()
        e.insert(0 , 'Cannot perform calculation now!')




my_button1 = Button(root , text='1', command=lambda : click(1), padx=30 , pady=20 , background='wheat')
my_button2 = Button(root , text='2', command=lambda : click(2), padx=30 , pady=20 , background='wheat')
my_button3 = Button(root , text='3', command=lambda : click(3), padx=30 , pady=20 , background='wheat')
my_button4 = Button(root , text='4', command=lambda : click(4), padx=30 , pady=20 , background='wheat')
my_button5 = Button(root , text='5', command=lambda : click(5), padx=30 , pady=20 , background='wheat')
my_button6= Button(root , text='6', command=lambda : click(6), padx=30 , pady=20 , background='wheat')
my_button7 = Button(root , text='7', command=lambda : click(7), padx=30 , pady=20 , background='wheat')
my_button8 = Button(root , text='8', command=lambda : click(8), padx=30 , pady=20 , background='wheat')
my_button9 = Button(root , text='9', command=lambda : click(9), padx=30 , pady=20 , background='wheat')
my_button0 = Button(root , text='0', command=lambda : click(0), padx=30 , pady=20 , background='wheat')
my_button10 = Button(root , text='+', command=add, padx=30 , pady=20 , background='wheat')
my_button11 = Button(root , text='Clear', command=clear_all, padx=59 , pady=20 , background='white')
my_button12 = Button(root , text='=', command=calc, padx=69, pady=20 , background='grey')


#put buttons on the screen
my_button1.grid(row=4 , column=0)
my_button2.grid(row=4 , column=1)
my_button3.grid(row=4 , column=2)

my_button4.grid(row=3 , column=0)
my_button5.grid(row=3 , column=1)
my_button6.grid(row=3 , column=2)

my_button7.grid(row=2,column=0)
my_button8.grid(row=2,column=1)
my_button9.grid(row=2,column=2)

my_button0.grid(row=5 , column=0)
my_button10.grid(row=6 , column=0)


my_button11.grid(row=5, column=1, columnspan=2)#clear

my_button12.grid(row=6 , column=1 , columnspan=2) #equal button





#the text input buttons







root.mainloop()