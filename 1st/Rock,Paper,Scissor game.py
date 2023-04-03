'''


                                                                            ##
 #####   ####   ####  #    #        #####    ##   #####  ###### #####      #  #       ####   ####  #  ####   ####   ####  #####   ####
 #    # #    # #    # #   #         #    #  #  #  #    # #      #    #      ##       #      #    # # #      #      #    # #    # #
 #    # #    # #      ####          #    # #    # #    # #####  #    #     ###        ####  #      #  ####   ####  #    # #    #  ####
 #####  #    # #      #  #   ###    #####  ###### #####  #      #####     #   # #         # #      #      #      # #    # #####       #
 #   #  #    # #    # #   #  ###    #      #    # #      #      #   #     #    #     #    # #    # # #    # #    # #    # #   #  #    #
 #    #  ####   ####  #    #  #     #      #    # #      ###### #    #     ###  #     ####   ####  #  ####   ####   ####  #    #  ####
                             #

'''
import random
print("Enter your choice")
choice = (['Rock', 'Paper', 'Scissor'])
computer = random.choice(choice)
user = str(input()).title()
if choice == computer:
    print('Tie')
elif computer== 'Rock'and user == 'Paper':
    print('user won')
elif computer== 'Paper' and user == 'Scissor':
    print('User won')
elif computer== 'Scissor' and user == 'Rock':
    print('user won')
else:
    print('computer won')
print("computer:",computer
      ,"\n user:",user)

