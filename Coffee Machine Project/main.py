from menu import MENU


def report_prompt():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def check_resources(user_i):
    # check against the resources
    for ingredient in MENU[user_i]["ingredients"]:
        if MENU[user_i]["ingredients"][ingredient] >= resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def check_transaction(user_i, quarter, dimes, nickles, pennies):
    global money
    total_input = 0.25 * quarter + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    cost = MENU[user_i]["cost"]
    if total_input < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        money += cost
        if total_input > cost:
            print(f"Here is {(total_input - cost):.2f} dollars in change.")
        return True


def make_drink(user_i):
    for ingredient in MENU[user_i]["ingredients"]:
        resources[ingredient] -= MENU[user_i]["ingredients"][ingredient]


machine = True
resources = {
    "water": 500,
    "milk": 300,
    "coffee":  200,
}
money = 0


while machine:
    u_quarters = 0
    u_dimes = 0
    u_nickles = 0
    u_pennies = 0
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "report":
        report_prompt()
    elif user_input == "off":
        machine = False
    elif user_input in MENU.keys():
        if check_resources(user_input):
            print("Please insert coins.")
            u_quarters = int(input("How many quarters?: "))
            u_dimes = int(input("How many dimes?: "))
            u_nickles = int(input("How many nickles?: "))
            u_pennies = int(input("How many pennies?: "))
            m_check = check_transaction(user_input, u_quarters, u_dimes, u_nickles, u_pennies)
            if m_check:
                make_drink(user_input)
                print(f"Here is your {user_input}. Enjoy!")

    else:
        print("Please enter a valid input")
