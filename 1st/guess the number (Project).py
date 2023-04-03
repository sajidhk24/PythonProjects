is_game_on = True
import random
from replit import clear


# number guessing game
# to get random numbers for guessing
def Random_gussed_game():
    '''Returns the random gussed number'''
    Level = input("Enter your difficulty number, 'e' for Easy\
    'm' for Medium and 'h'for Hard :\n")
    if Level == 'e':
        R = 20
    elif Level == 'm':
        R = 50
    else:
        R = 100
    number  = random.randint(1,R)
    return number
    #print(Gussed_Number)


Random_number = []
Random_number.append(Random_gussed_game())
number_of_guesses=1
print("Number of guesses is limited by 9 times; ")
while is_game_on==True:
    attempted =[]
    while(number_of_guesses<=9):
        Guess_the_number = [int(input("guess the number \n"))]
        if Guess_the_number < Random_number:
            print("please enter bigger number\n")
            attempted.append(Guess_the_number)
        elif Guess_the_number > Random_number:
            print("Please enter smaller number\n")
            attempted.append(Guess_the_number)
        else:
            print("you won \n")
            print(number_of_guesses,"number of guesses took to finish")
            break
        print(9-number_of_guesses, "number of guesses left")
        number_of_guesses= number_of_guesses+1
        if(number_of_guesses>9):
            print('Game over')
        if input('You want to play the game again,Type "y" else "n":\n') == 'y':
             is_game_on = True
             clear()
        else:
            is_game_on = False
            print(attempted)
##########################################################################
