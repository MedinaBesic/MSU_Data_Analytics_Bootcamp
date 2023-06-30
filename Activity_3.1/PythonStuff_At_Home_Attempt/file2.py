
options = ['p', 'r', 's']

winner=[]

game = 'y'

while game == 'y':
    my_choice=input('select p, r, or s ')
    
    computer_choice = random.choice(options)

    if my_choice == computer_choice:
        print("It's a tie ")

    elif my_choice == 'r' and computer_choice == 's':
        print("You win! ")
        Winner = 'You'
    elif my_choice == 'r' and computer_choice == 'p':
        print("You lose! ")
        Winner = 'Computer'

    #print(f'You have selected {my_choice}')

    winner.append(winner)
#the indentation is important or it won't work 
    game = input('Do you want to continue with the game? y or n ')



L = ['a', 'b', 'c', 'd', 'e']

#adding values to a list 
L.append('k')

#removing values from a list 
#L.pop()











# #to check if x is in the list 
# if x in L:
#     print('x is in the list L')

# else:
#     print('x is not in the list L')


# #whatever is in the [] is the index it is referencing 
# if x == L[4]:
#     print('they are equal ')

# else:
#     print()