import datetime
import logging


def logger_info(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__), level= logging.INFO)

    def wrapper_function(*args, **kwargs):
        logging.info("Run in time: {}".format(choice.get()))
        return original_function(args, kwargs)
    return wrapper_function


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

try:
    # check if resource is sufficient or not
    def is_sufficient(ordered_ingredients):
        for item in ordered_ingredients:
            if Resources[item] >= ordered_ingredients[item]:
                return True
            else:
                print(f'Sorry, Insufficient, {item}')
                return False


    def process_money(drink_cost):
        global profit
        print('Please Insert Coins')
        money = int(input('How many coins of 5 rs: ')) * 5
        money += int(input('How many coins of 10 rs: ')) * 10
        money += int(input('How many coins of 100rs: ')) * 100
        profit += money
        if money >= drink_cost:
            change = round(money - drink_cost, 2)
            print(f'Here is your change amount: {change}')
            return True
        else:
            return 'Insufficient Money, Unable to process!'

    @logger_info
    def make_coffee(Resources, ordered_ingredients):
        for item in ordered_ingredients:
            Resources[item] -= ordered_ingredients[item]
        print(f'Enjoy your {choice}!')


    profit = 0
    is_on = True
    while (is_on):
        choice = input('Enter your choice: (Latte/Cappiccino/Espresso:  ').title()
        if choice == 'report':
            print(f"Water: {Resources['Water']}ml")
            print(f"Milk: {Resources['Milk']}ml")
            print(f"Coffee: {Resources['Coffee']}gms")
        elif choice == 'off':
            is_on = False
        else:
            drink = menu[choice]
            print('You have choosed: ', drink)
            if is_sufficient(drink['ingredients']):
                if process_money(drink['cost']):
                    make_coffee(Resources, drink['ingredients'])

except Exception as e:
    print(e)
