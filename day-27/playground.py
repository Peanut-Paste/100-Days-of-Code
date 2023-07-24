# unlimited positional argument
def add(*args):
    print(args[1])
    total = 0
    for n in args:
        total += n
    return total


a = add(3, 5, 5, 5, 5)
print(a)

# unlimited keyword argument


def calculated(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n *= kwargs["multiply"]
    n += kwargs["add"]
    print(n)


calculated(2, add=3, multiply=5)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("colour")
        self.seats = kwargs.get("seats")

my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)
print(my_car.make)