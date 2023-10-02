from menu import Menu
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker
menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()


def machine():
    machine_on = True
    while machine_on:
        result = input("What would you like? (espresso/latte/cappuccino/): ").lower()
        if result == "off":
            machine_on = False
        elif result == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(result)
            if result == "latte":
                output = 0
            elif result == "espresso":
                output = 1
            else:
                output = 2
            if coffee_maker.is_resource_sufficient(drink):
                menu_item = menu.menu[output]
                total = menu_item.cost
                if money_machine.make_payment(total):
                    coffee_maker.make_coffee(drink)


machine()
