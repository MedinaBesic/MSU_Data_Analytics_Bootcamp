names = ['a','b', 'c', 'd']

#len(names)

#we created a new variables items to iterate through names list 
#for items in names:
    #print(items)

#we are going to iterate through 10, but is starts at index 0, so it will print 0-9 in terminal 
#for i in range(10):
    #print(i)

n=len(names)

#n will be equal to four because that is how many items are in the list

#print(f'n is {n}')

#The following code will do the same thing as the line of code above
#print("n is {}"".format(n))

#i is the indexes, in this case 3, n is the number of items in the list 

# for i in range(n):
#     print(names[i])

#if you want to only iterate through a certain number of items in the list
#for i in range(2):
    #print(names[i])

#--------------------------------------------------------------------------

#you can import libraries to help with code
import random

L= ['a','b', 'c', 'd', 'e']

#out of the list above, the computer will pick an item at random
pick = random.choice(L)

# print(pick)

options = ['p', 'r', 's']

my_choice = input("Make your selection from either r, p, or s ")

#this line of code is to ensure that my choice is either r, p, or s... else
if my_choice not in options:
    print('This is an invalid selection. Please select either r, p or s.')

print(f"You selected {my_choice}.")

computer_choice = random.choice(options)

if my_choice == 'r' and computer_choice == 's':
    print("You won!")

elif my_choice == computer_choice:
    print("It's a tie!")

elif my_choice == 'r' and computer_choice == 'p':
    print("You lost!")









                  

