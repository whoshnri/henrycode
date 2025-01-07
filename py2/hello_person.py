def hello(name, lang):
    
    greetings = {
        "English" : 'Hello',
        "Spanish" : "Hola",
        "German" : "Halo"
    }
    greeting = f'{greetings[lang]} {name}'

    print(greeting)

if __name__ == '__main__':


    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personal greeting."
    )
    parser.add_argument(
        '-l' , '--lang' , metavar='language' ,
        required=True , help="This is the language of the greeting.",
        choices=["English" , 'Spanish' , "German"]

    )
    parser.add_argument(
        '-n' , '--name' , metavar="name",
        required=True ,help="The name of the person to greet."
    )

    args = parser.parse_args()

    hello(args.name , args.lang)


