"""This is a python rock, paper, scissors game in which the user
will play a game against the computer."""

import random

#variable definitions
choice_options = ['Rock', 'Paper', 'Scissors']
game_on = 1
user_choice = ''
computer_choice = ''
game_status = 1

#function definitions
def user_input():
    user_input = ''
    while user_input not in choice_options:
        user_input = input('What is your choice? Please choose Rock, Paper, or Scissors!: ').capitalize()
        if user_input not in choice_options:
            print('Sorry, Invalid Input!')
    return user_input

def computer_input():
    computer_input = random.choice(choice_options)
    return computer_input

def win_check(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Draw, try again!')
    elif (user_choice == 'Paper') and (computer_choice == 'Rock'):
        print('User Wins!')
    elif (user_choice == 'Rock') and (computer_choice == 'Scissors'):
        print('User Wins!')
    elif (user_choice == 'Scissors') and (computer_choice == 'Paper'):
        print('User Wins!')
    else:
        print('Computer Wins!')

def game_on():
    user_input = None
    viable_choices = ['Y','N']
    while user_input not in viable_choices:
        user_input = input('Would you like to keep playing? Y/N?: ').capitalize()
        if user_input not in viable_choices:
            print('Sorry, Invalid Input!')
    if user_input == 'Y':
        return 1
    else:
        return 0
    
def play():
    user_choice = user_input()
    computer_choice = computer_input()
    print(f'The computer chose {computer_choice}')
    win_check(user_choice, computer_choice)

print('Welcome to Rock, Paper, Scissors, in Python! Can you best the computer?')   
while game_status:
    play()
    game_status = game_on()
    