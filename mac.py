import emoji

menu = {
    'Latte': {
        'ingredients': {
            'Water': 150,
            'Coffee': 24,
            'Milk': 200,
        },
        'cost': 200,
    },
    'Espresso': {
        'ingredients': {
            'Water': 50,
            'Coffee': 18,
        },
        'cost': 150,
    },
    'Cappiccino': {
        'ingredients': {
            'Water': 250,
            'Coffee': 24,
            'Milk': 200,
        },
        'cost': 250,
    }
}

Resources = {
    'Water': 200,
    'Milk': 300,
    'Coffee': 76,
}


# check if resource is sufficient or not
def is_sufficient(ordered_ingridient):
    for item in ordered_ingridient:
        if Resources[item] >= ordered_ingridient[item]:
            return True
        else:
            print(f"Sorry! Insufficient, {item}")
            return False


def process_money(drink_cost):
    global profit
    print(f"Enter the amount of {drink_cost} ")
    money = int(input('How many coins of 5 rs: ')) * 5
    money += int(input('How many coins of 10 rs: ')) * 10
    money += int(input('How many coins of 100rs: ')) * 100
    profit += money
    if money >= drink_cost:
        change = round(money - drink_cost, 2)
        print(f"Here is your change amount of {change} ")
        return True
    else:
        return 'insufficient amount, unable to process'


def make_coffee(resources, ordered_ingredient):
    for item in ordered_ingredient:
        resources[item] -= ordered_ingredient[item]
    print(f"Enjoy your {choice} ")
    print(emoji.emojize(":grinning_face_with_big_eyes:"))


profit = 0
is_on = True
while is_on:
    choice = input('Enter your choice: (Latte/Cappiccino/Espresso:  ')
    if choice == 'report':
        print(f"Water: {Resources['Water']}ml")
        print(f"Milk: {Resources['Milk']}ml")
        print(f"Coffee: {Resources['Coffee']}gms")
        print(f"Profit is {profit}")

    elif choice == 'off':
        is_on = False

    else:
        drink = menu[choice]
        if is_sufficient(drink['ingredients']):
            if process_money(drink['cost']):
                make_coffee(Resources, drink['ingredients'])
