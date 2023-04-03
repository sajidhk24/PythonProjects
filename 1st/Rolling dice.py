# To make a rolling dice
import random
while (True):
    value = random.randint(1,6)
    throw_the_dice = value
    print("player 1\n", throw_the_dice)
    if value == 6:
        print('Again chance for Player 1')
        continue
    else:
        print("chance for player 2")
        print(random.randint(1,6))
    break



