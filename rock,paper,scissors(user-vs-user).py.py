"""This is rock, paper, scissors in Python! This program is a two player game, in which the two users can compete
in rock paper scissors!"""

import os

choice_options = ['Rock', 'Paper', 'Scissors']
game_on = 1
user1_choice = ''
user2_choice = ''
game_status = 1
#function that accepts user input
def user_input():
    user_input = ''
    while user_input not in choice_options:
        user_input = input('What is your choice? Please choose Rock, Paper, or Scissors!: ').capitalize()
        if user_input not in choice_options:
            print('Sorry, Invalid Input!')
    return user_input

#function that checks if the game has been won
def win_check(user1_choice, user2_choice):
    if user1_choice == user2_choice:
        print('Draw, try again!')
    elif (user1_choice == 'Paper') and (user2_choice == 'Rock'):
        print('User 1 Wins!')
    elif (user1_choice == 'Rock') and (user2_choice == 'Scissors'):
        print('User 1 Wins!')
    elif (user1_choice == 'Scissors') and (user2_choice == 'Paper'):
        print('User 1 Wins!')
    else:
        print('User 2 Wins!')

#function that determines game state
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

#function which clears the screen during the game
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#function that plays the game
def play():
    print('User 1, please enter:')
    user1_choice = user_input()
    cls()
    print('User 2, please enter:')
    user2_choice = user_input()
    print(f'User 1 chose: {user1_choice}')
    print(f'User 2 chose: {user2_choice}')
    win_check(user1_choice, user2_choice)

#while loop that maintains the game until the user terminates the program
print('Welcome to Rock, Paper, Scissors, in Python!')   
while game_status:
    play()
    game_status = game_on()