print("Welcome in Treasure Island.")
print('Your mission is to find the Treasure!')
choice1 = input('You are at cross-road, Where do you want to go? LEFT OR RIGHT\n')
choice1 = choice1.upper()
if choice1 == 'RIGHT':
    print('You fell into a hole,"Game over!"')
    choice2 = input('You have come to a lake. There is an island in the middle of the lake.Type "wait" to wait for a boat. Type "swim" to swim across.').upper()
    if choice2 =="WAIT":
        choice3 = input('')
    else:
        print('You attacked by trout."Game Over"!')

elif choice1 =='LEFT':
    print('You can continue game')