
#print("Hello")
#x=50
#y=20
#name='John'
#print("My name is " + name)
#print("My age is " + str(y))
#print("Again, my age is {}".format(y))
#print(x+y)

#name = input("What is your name? ")

#print("You entered " + name + ". Is this true?")
#---------------------------------------------------------------
from re import L


x=int(input("What is your age? "))

y=int(input("What is your height? "))

sum_of_ages= x+y

#Another way to print the following statement is:
print("Both of your ages add to {}".format(sum_of_ages))
#is: print("Both of your ages add to " + str(sum_of_ages))

#Conditional statement 

if x < 20:
    age_group= "Young"

elif x >= 20 and x < 40:
    age_group="Older"
else:
    age_group="Very old"

#The folllowing code
# print("You belong to {} age group".format(age_group))
#is the same as:
print(f'You belong to {age_group}')


if y > 6 and x > 40:
    print("y is greater than 20")

else:
    print("y is less than 20")


