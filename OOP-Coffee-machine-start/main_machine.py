from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
money_machine.report()
is_on = True

coffee_maker = CoffeeMaker()
coffee_maker.report()

menu = Menu()


while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        is_enough_money = money_machine.make_payment(drink.cost)
        if is_enough_money and is_enough_ingredients:
            coffee_maker.make_coffee(drink)





