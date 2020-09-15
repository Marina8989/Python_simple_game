print('Welcome to my first game!')

name = input('What is you name? ')
age = int(input('What is your age? '))
if age >= 18:
    print('You are old enough to play!')
    play = input('Do you want to play? ').lower()
    if play == 'yes':
        print('You are starting with 10 health')
        print('Let\'s play!')
        choice = input('First choice... Left or Right? ').lower()
        if choice == 'left':
            
    else:
        print('Game over')    

else:
     print('Sorry, you are not old enough to play!')   

