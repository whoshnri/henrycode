from random import  choice as c

capital = 'Topeka'

bird = 'Western MedowLark'

flower = 'Sunflower'

song = 'Home on the range'

def randomfunfacts():
    funfacts =[

        "Kansas is considered flat but it does have some mountains",
        "Wichita is the largest city in the state but many may guess Kansas City",
        "A considerable portion of Kansas City is actually i Missouri",
        "Most Kansans are annoyed by Wizard of Oz references from people outside of Kansas"
    
    ]
    index = c([0,1,2,3])

    print(funfacts[index])


if __name__ == '__main__' :
    randomfunfacts()    #its important to do this--this is to mae sure something always returns from a module when it is active
    