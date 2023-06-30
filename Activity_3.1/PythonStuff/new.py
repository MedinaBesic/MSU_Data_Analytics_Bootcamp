names = ['a', 'b', 'c', 'd']


# len (names)

# for item in names:
  # print(item)

#for i in range(10):
    #print(i)

# n=len(names)

# print(f'n is {n}')
# this is the same as the line above, for reference: print('n is {}'.format(n))


# n=len(names)

# for i in range(2):
#    print(names[i])

#    names[2]

import random

L=['a', 'b', 'c', 'd', 'e']

pick = random.choice(L)

#print(pick)

options=['p', 'r', 's']

my_choice= input('make your selection from either: r, p or s')

if my_choice not in options:
    print('invalid selection. Please select either r, p or s')

    print(f'you selected {my_choice}')

computer_choice = random.choice(options)

if my_choice == random.choice(options)
print("It's a tie")

elif my_choice == 'r' and computer_choice == 's'
print('You win!')

elif my_choice == 'r' and computer_choice == 'p'
print('You lose!')

elif my_choice == 'p' and computer_choice == 's'
print('You lose!')


