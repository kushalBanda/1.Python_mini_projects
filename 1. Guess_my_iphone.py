# Guess my iphone game
print("Welcome to Guess your iphone Quiz")
print("I will try to guess your iphone model , based on the information , I receive from you")

playing = input('Do you want to play? : ')
if playing.lower() == 'yes':
    print("Okay, Let's play!")

    Year = input(
        "What's the Year of Production of your iphone?(Expecting an integer) : ")
    while Year.isnumeric() != True:
        Year = input('Expecting an integer : ')
    if (Year == '2020'):
        print("It's an iphone 12 series")
        camera = input(
            'Enter the number of cameras on the back of your iphone 12 series : ')
        while camera.isnumeric() != True:
            input('Expecting a natural number : ')
        if camera == '2':
            print("It's an iphone 12")
            print('Thank you for playing this quiz')
            quit()
        elif camera == '3':
            print("It's either an iphone 12 Pro or an iphone 12 Pro Max")
            print('Thank you for playing this quiz')
            quit()
        else:
            print("Too good to be True")
            quit()
    elif (Year == '2019'):
        print("It's an iphone 11 series")
        camera = input(
            'Enter the number of cameras on the back of your iphone 11 series : ')
        while camera.isnumeric() != True:
            input('Expecting a natural number : ')
        if camera == '2':
            print("It's an iphone 11")
            print('Thank you for playing this quiz')
            quit()
        elif camera == '3':
            print("It's either an iphone 11 Pro or an iphone 11 Pro Max")
            print('Thank you for playing this quiz')
            quit()
        else:
            print("Too good to be True")
            quit()
    elif (Year == '2018'):
        print("It's an iphone 10 series")
        camera = input(
            'Enter the number of cameras on the back of your iphone 10 series : ')
        while camera.isnumeric() != True:
            input('Expecting a natural number : ')
        if camera == '1':
            print("It's an iphone 10")
            print('Thank you for playing this quiz')
            quit()
        elif camera == '2':
            print("It's either an iPhone XS or an iPhone XS Max")
            print('Thank you for playing this quiz')
            quit()
        else:
            print('Too good to be True')
            quit()
    else:
        print("Your iphone is too old to be guessed , time to get a new one")
        quit()
else:
    quit()
