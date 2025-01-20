#this is for password manipulation
# a mini version of cryptography that i worked on while i was busy



import random

def isEven(num):
    if num % 2 == 0:
        return True
    else :
        return False

def manipulate(letter):
    alphabet = ['abcdefghijklmnlopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    numbers = '123456789'
    signs = '!@$#%^&*()-_+="\':;,<>/?}{[]}|'
    global newgen
    newgen = ''
    let = letter
    if let in alphabet[0]: #lowecase
        index = alphabet[0].index(let)
        if isEven(index):
            newgen = alphabet[1][int(index/2)]
        else:
            newgen = alphabet[1][(index - 1)]
    if let in alphabet[1]: #uppercase
        index = alphabet[1].index(let)
        if isEven(index):
            newgen = alphabet[0][int(index/2)]
        else:
            newgen = alphabet[0][index - 1]
    return newgen


def crypt(passwd):
    p_list = list(passwd)
    strpass = ''
    for i in p_list:
        strpass += manipulate(i)

    print(strpass)

    

input = input('Enter a password: ')
crypt(input)