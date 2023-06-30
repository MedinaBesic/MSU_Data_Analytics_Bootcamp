


# name = input('what is your name ?')


# print('You entered ' + name + ' is this true?')


x=int(input('what is your age? '))

y=int(input('What is your height? '))


sum_of_ages=x+y


print('both of your ages add to {}'.format(sum_of_ages))


#conditional statement

if x < 20:
    age_group= 'Young'
elif x >= 20 and x < 40:
    age_group= 'Older'
else:
    age_group= 'Very Old'

print('You belong to {} group'.format(age_group))



if y > 6 and x > 40:
    print('You are really tall')
else:
    print("it's good")