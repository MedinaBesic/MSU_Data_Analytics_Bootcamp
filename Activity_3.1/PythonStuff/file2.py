L = ['a', 'b', 'c', 'd', 'e']


game = 'y'

winner = []

options = ['p','r','s']
while game == 'y':
    my_choice = input('select p, or r, or s')
    computer_choice=random.choice(options)

    #print('You selected' {}.format(my_choice}))

    if my_choice == computer_choice:
        print('It's a tie)

    elif my_choice == 'r' and computer_choice == 's':
        winner = 'You'
        print('You win!')

    elif my_choice == 'r' and computer_choice == 'p':
        winner = 'Computer'
        print('You win!')

winner.append(winner)

game=input('Do you wnat to continue with the game? y or n')

#This is what the append function does: winner = ['You', 'You', 'Computer'] ; it adds value to a list
#The above is hypothetical what the comp does if you played three games 

L = ['a', 'b', 'c', 'd', 'e']


#adding values in a list 
L.append('k')

#remove values from a list, where pop uses index to determine which variable is removed from the list
L.pop(0)

