# Take input of you and your neighbor
my_name=input("What is your first name? ")

neighbors_name=input("What is your neighbor's first name? ")


# Take how long each of you have been coding

my_coding=int(input("How long have you been codding? "))

neighbors_coding=int(input("How long has your neighbor been coding? "))

# Add total month
total= int(my_coding) + int(neighbors_coding) 


# Print results
#print(f'{my_name} has been coding for {my_coding} month and her neighbor, {neighbors_name}, has been coding for {neighbors_coding} years.')
print("I am " + my_name + " and my neighbor is " + neighbors_name + ".")

print("Together we have been coding for " + str(total) + " months!") 

