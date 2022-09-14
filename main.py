"""
this is the most basic form of the guessing game
"""

import random

MAX_NUMBER = 10  # max number
MIN_NUMBER = 1  # min number

# making random number
random_number = int(random.randint(MIN_NUMBER, MAX_NUMBER))

while True:  # main game loop
    try:
        # asking use for an number
        user_answer = int(input(
            f'guess a number bettween {MIN_NUMBER} and {MAX_NUMBER}: '
        ))
        if(user_answer == random_number):  # they guessed the number
            print('you have guessed the number!!!')

        # the number is too small or too big
        elif(user_answer < MIN_NUMBER) or (user_answer > MAX_NUMBER):
            print(f'that number is not bettween {MIN_NUMBER} and {MAX_NUMBER}')
        # if number is bigger than the random number
        elif(user_answer > random_number):
            print('that number is too big')
        # if number is smaller that the random number
        elif(user_answer < random_number):
            print('that number is to small')
        else:  # anything else
            print('that is not an answer i can use')
            print(f'guess a number {MIN_NUMBER} and {MAX_NUMBER}')

    except ValueError:  # if they dont user a number
        print('that is not an answer i can use')
        print(f'guess a number {MIN_NUMBER} and {MAX_NUMBER}')
