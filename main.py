"""
this is the most basic form of the guessing game

"""


import random 

MAX_NUMBER= 10 #max number
MIN_NUMBER = 1 #min number 

random_number = int(random.randint(MIN_NUMBER, MAX_NUMBER)) #making random number 

#this is just to help me so i know what the number is 
#print(random_number)
while True: #main game loop 
    try:
        #asking use for an number 
        user_answer = int(input('guess a number bettween {} and {}: '.format(MIN_NUMBER, MAX_NUMBER)))
        
        if(user_answer == random_number): #they guessed the number
            print('you have guessed the number!!!')

        elif(user_answer < MIN_NUMBER) or (user_answer > MAX_NUMBER): #the number is too small or too big  
            print('that number is not bettween {} and {}'.format(MIN_NUMBER, MAX_NUMBER))

        elif(user_answer > random_number): #if number is bigger than the random number
            print('that number is too big')
        
        elif(user_answer < random_number):#if number is smaller that the random number 
            print('that number is to small')

        else: #anything else 
            print('that is not an answer i can use')
            print('guess a number {} and {}'.format(MIN_NUMBER, MAX_NUMBER))

    except ValueError: #if they dont user a number 
        print('that is not an answer i can use')
        print('guess a number {} and {}'.format(MIN_NUMBER, MAX_NUMBER))














