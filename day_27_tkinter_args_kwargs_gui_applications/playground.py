# position arguments example by *args
# def add(*args):
#     sum = 0
#     for num in args:
#         sum += num
#     return sum

# print(add(1,3,5))

# keyword arguments example by **kwargs
def calculate(n, **kwargs):
    # print(n)
    # print(kwargs)
    for key, value in kwargs.items():
        print(key, value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(7, add=1, multiply=2) # here 7 is positional argument and add, multiply is keyword argument

# dealing with keyword arguments in OOPS
class Car:
    def __init__(self, **kw) -> None:
        self.make = kw.get("make")  # get() will return value if key is found else return None
        self.model = kw.get("model")
my_car = Car(make="Nissan")
print(my_car.model)