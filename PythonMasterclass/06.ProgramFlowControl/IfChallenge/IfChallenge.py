name = input('What is your name? ')
age = int(input('How old are you dear {0}? ' . format(name)))

if 18 <= age < 31:
    print('Welcome to the club 18-30 holidays dear {0}' . format(name))
else:
    print('Sorry {0} you are not allowed to get in the club'
          ', because you are {1}' . format(name, age))