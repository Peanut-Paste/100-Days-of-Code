from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
machine = CoffeeMaker()
money = MoneyMachine()
is_on = True

while is_on:
    userinput = input(f"What would you like? ({menu.get_items()}: ").lower()
    if userinput == "off":
        is_on = False
    elif userinput == "report":
        machine.report()
        money.report()
    else:
        item = menu.find_drink(userinput)
        if item is None:
            ""
        else:
            if machine.is_resource_sufficient(item) and money.make_payment(item.cost):
                machine.make_coffee(item)

