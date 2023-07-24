from data_manager import DataManager

sheety = DataManager()

is_on = True

while is_on:
    first_name = input("What's your first name?")
    last_name = input("What's your last name?")
    email = input("What's your email?")
    verification = input("Key in your email again")
    if email == verification:
        is_on = False
        sheety.add_row(first_name, last_name, email)
        print("Welcome to the flight club!")
    else:
        print("The email you keyed in is different")


