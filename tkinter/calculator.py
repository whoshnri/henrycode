from tkinter import *

root = Tk()

root.title("Simple Calculator")

e = Entry(root , width=50 , borderwidth=2,)

e.grid(row=0 , column=0 , columnspan=4, padx=5, pady=20 , rowspan=3)

vals = [] #stores the input already oassed to the screen....
op = []#stores the active operator
ans = [0] #stores the answer


def click(num):
    if e.get() in ['+' , '-' , '/' , '*'] and num in ['+' , '-' , '/' , '*']:
        clear()
        e.insert(0, num)

    elif e.get() not in ['+' , '-' , '/' , '*'] and num not in ['+' , '-' , '/' , '*'] :
        current = e.get()
        clear()
        e.insert(0 , f'{current}{num}')
    
    
    else:
        clear()
        e.insert(0 ,num)




    
      
def add():
    if '+' in op or '-' in op or '/' in op or '*' in op:
        calc()
        op.append('+')
        print(op)
        clear()
        e.insert(0 , '+')

    elif e.get() in ['+' , '-' , '/' , '*']:
        op.pop()
        op.append('+')
        print(op)
        clear()
        e.insert(0, '+')
    else:
        vals.append(float(e.get()))
        print(vals)
        op.append('+')
        print(op)
        clear()
        e.insert(0 , '+')
             
def subtract():
    if '+' in op or '-' in op or '/' in op or '*' in op:
        calc()
        op.append('-')
        print(op)
        clear()
        e.insert(0 , '-')

    elif e.get() in ['+' , '-' , '/' , '*']:
        op.pop()
        op.append('-')
        print(op)
        clear()
        e.insert(0, '-')

    else:
        vals.append(float(e.get()))
        print(vals)
        op.append('-')
        print(op)
        clear()
        e.insert(0 , '-')
        
def divide():
    if '+' in op or '-' in op or '/' in op or '*' in op:
        calc()
        op.append('/')
        print(op)
        clear()
        e.insert(0 , '/')

    elif e.get() in ['+' , '-' , '/' , '*']:
        op.pop()
        op.append('/')
        print(op)
        clear()
        e.insert(0, '/')

    else:
        vals.append(float(e.get()))
        print(vals)
        op.append('/')
        print(op)
        clear()
        e.insert(0 , '/')

def multiply():
    if '+' in op or '-' in op or '/' in op or '*' in op:
        calc()
        op.append('*')
        print(op)
        clear()
        e.insert(0 , '*')

    elif e.get() in ['+' , '-' , '/' , '*']:
        op.pop()
        op.append('*')
        print(op)
        clear()
        e.insert(0, '*')

    else:
        vals.append(float(e.get()))
        print(vals)
        op.append('*')
        print(op)
        clear()
        e.insert(0 , '*')
    

def clear():
    e.delete(0 , END)


def clear_all():
    clear()
    vals.clear()
    op.clear()
    ans.clear()
    ans.append(0)
    ans.append(0)


def calc(E = e):
    if '+' in op:
        vals.append(float(E.get()))
        print(vals)
        result = vals[-2] + vals[-1]
        op.clear()
        vals.clear()
        vals.append(result)
        print(vals)
        clear()
        E.insert(0 , result)
        ans.append(result)
    if '-' in op:
        vals.append(float(E.get()))
        print(vals)
        result = vals[-2] - vals[-1]
        op.clear()
        vals.clear()
        vals.append(result)
        print(vals)
        clear()
        E.insert(0 , result)
        ans.append(result)
    if '*' in op:
        vals.append(float(E.get()))
        print(vals)
        result = vals[-2] * vals[-1]
        op.clear()
        vals.clear()
        vals.append(result)
        print(vals)
        clear()
        E.insert(0 , result)
        ans.append(result)
    if '/' in op:
        try:
            vals.append(float(E.get()))
            print(vals)
            result = vals[-2] / vals[-1]
            op.clear()
            vals.clear()
            vals.append(result)
            print(vals)
            clear()
            E.insert(0 , result)
            ans.append(result)
        except ZeroDivisionError as e:
            print(f'Error: {e}')
            clear_all()
    



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
plus_button = Button(root , text='+', command=add, padx=29 , pady=20 , background='wheat')
subtract_button = Button(root , text='-', command=subtract, padx=30 , pady=20 , background='wheat')
divide_button = Button(root , text='/', command=divide, padx=30 , pady=20 , background='wheat')
multiply_button = Button(root , text='*', command=multiply, padx=30 , pady=20 , background='wheat')
my_button11 = Button(root , text='Clear', command=clear_all, padx=60 , pady=20 , background='white')
my_button12 = Button(root , text='=', command=calc, padx=150, pady=20 , background='grey')


#put buttons on the screen
my_button1.grid(row=5 , column=0)
my_button2.grid(row=5 , column=1)
my_button3.grid(row=5 , column=2)
divide_button.grid(row=5 , column=3)


my_button4.grid(row=4 , column=0)
my_button5.grid(row=4 , column=1)
my_button6.grid(row=4 , column=2)
subtract_button.grid(row=4 , column=3)

my_button7.grid(row=3,column=0)
my_button8.grid(row=3,column=1)
my_button9.grid(row=3,column=2)
plus_button.grid(row=3 , column=3)


multiply_button.grid(row=6 , column=3)
my_button0.grid(row=6 , column=0)
my_button11.grid(row=6, column=1, columnspan=2)#clear

my_button12.grid(row=7 , column=0 , columnspan=4) #equal button





#the text input buttons





root.mainloop()