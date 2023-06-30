# # Number Chain

# In this activity, you will take user input and print out a string of numbers.

# ## Instructions

# * Using a `while` loop, ask the user "How many numbers?", and then print out a chain of numbers in increasing order, from 0 to the user-input number.

# * After the results have been printed, ask the user if they would like to continue.

#     * If "y" is entered, keep the chain running by inputting a new number and starting a new count from 0 to the new user-input number.

#     * If "n" is entered, exit the application.

# ## Bonus

# Rather than just displaying numbers starting from 0, have the numbers begin at the end of the previous chain.

user_play = 'y'

#set start number
start_number = 0 

while user_play == 'y':
    #ask how many numbers to loop through
    user_input = int(input("How many numbers?" ))

    #loop thru the numbers (be sure to cast the string into an int)
    for x in range(start_number, user_input + start_number):
        #print each number in the range
        print(x)

    #set the next start number as the last number of the loop 
    start_number= start_number + user_input 

    #once complete
    user_play = input (" Continue the chain: (y) or (n)? ")

