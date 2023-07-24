# # Function inputs/functionality/output
#
# def add(n1, n2):
#     return n1 + n2
#
# def subtract(n1, n2):
#     return n1 - n2
#
# def multiply(n1, n2):
#     return n1 * n2
#
# def divide(n1, n2):
#     return n1/n2
#
# # Functions are First-class object, can be passed around as arguments e.g. int/string/float etc.
#
# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)
#
# result = calculate(add, 2, 3)
# print(result)
#
# # Nested Functions
#
# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm inner")
#
#     nested_function()
#
# outer_function()

# Functions can be returned from other functions

# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm inner")
#
#     return nested_function
#
# inner_function = outer_function()
# inner_function()
# import time
#
# def decorator(function):
#     def decoration():
#         time.sleep(2)
#         function()
#     return decoration
#
# @decorator
# def say_hello():
#     print("Hello")
#
# say_hello()

# Advanced Python Decorator Functions
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated(function):
    def wrapper(*args):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("Isaac")
new_user.is_logged_in = True
create_blog_post(new_user)

