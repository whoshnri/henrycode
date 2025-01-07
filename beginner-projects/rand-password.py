import random
import string


chars = list(string.ascii_letters + string.digits + '@!#$%^&*?')


def create_password(len , num , letter):
    password_str = ''
    password = []
    for x in range(letter):
        password.append(random.choice(string.ascii_letters))
    for x in range(num):
        password.append(random.choice(string.digits))
    for x in range(len - (num + letter)):
        password.append(random.choice('@!#$%&*-+?'))


    random.shuffle(password)
    for i in password:
        password_str += i
    print(f'Your new password is: {password_str}')
    
    

def validate():
    go = input('Do you want to create a new password?\n')
    if go.lower() not in ['yes' , 'y']:
        return
    go_int1 = int(input("Specify number of characters\n"))
    go_int2 = int(input('Enter number of numbers:\n'))
    if go_int1 > go_int2 :
        go_int3 = int(input('Enter number of letters:\n'))
        if (go_int1 - go_int2) >= go_int3:
            create_password(go_int1 , go_int2 , go_int3)
        else:
            print('Number is too large')
    else:
        print('Number is too large')


validate()
