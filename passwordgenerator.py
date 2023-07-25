"""This is a python script which generates a strong, random password based on user input"""

import random
import string

char_list = string.printable
num_list = [1,2,3,4,5,6,7,8,9]

#function which takes user input for the number of password to generate
def numpasswords():
    user_input = None
    while user_input not in num_list:
        user_input = int(input('How many passwords would you like to generate?: '))
        if user_input not in num_list:
            print('Sorry, Invalid Input')
    return user_input

#function which takes user input for the length of password to generate
def password_length():
    user_input = None
    while user_input not in num_list:
        user_input = int(input('How long would you like your passwords to be?: '))
        if user_input not in num_list:
            print('Sorry, Invalid Input')
    return user_input

#function which generates passwords based on the user defined criteria
def password_generator(num_of_passwords, length_of_passwords):
    password_count = num_of_passwords
    for i in range(0,num_of_passwords):
        password = ''
        for i in range(0,length_of_passwords):
            password += random.choice(char_list)
        print(password)

print('\n\nStrong Password Generator')
print('------------------------- \n')

password_generator(numpasswords(),password_length())