'''
Python code to a guess game named as 3 cup monte
where user have to guess that which galss contains the ball.
'''

from random import shuffle

def list_suffle(my_list):
    shuffle(my_list)
    return my_list

def user_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Pick a number: 0, 1 or 2")
    return int(guess)

def check_guess(my_list, guess):
    if my_list[guess] == 'O':
        print ("Correct guess")
    else:
        print ("incorrect guess, try again!!")
        print (my_list)

#INITIATE list
my_list = [' ', 'O', ' ']
#SHUFFLE list
suffled_list = list_suffle(my_list)
#USER GUESS
entered_guess = user_guess()
#CHECK GUESS
check_guess(suffled_list, entered_guess)
