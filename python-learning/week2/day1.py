"""
Functions - reusable block of code
Syntax: def function_name():

1. Default Arguments - uses the assigned values when it is not directly configured
2. *args - accept any number of extra positional values
3. *kwargs - accept any number of extra named values
"""

# Default Arguments
def greet(name, greeting="Hello"):  # The greeting parameter is default
    print(greeting, name)
greet("Jethro") # Hello Jethro
greet("Jethro",  "Ad Astra Abyssosque")  # Ad Astra Abyssosque Jethro

# *args - saves as tuple
def fav_things(name, *things):
    print(f"Hello {name}! You likes {" ".join(things)}.")

fav_things("Jethro", "Chess", "Genshin", "Hacking")

# **kwargs - saves as dict
def information(name, **extra_infos):
    print(f"Hello {name}! Here are other things about you:")
    print(extra_infos)

information("Jethro", age=19, color="Blue")

# Mini Challenges
def describe_pet(name, animal="dog"):
    print(f"You have a pet {animal}, and its name is {name}!")

describe_pet("Ramon")
describe_pet("Kidlat", "cat")

def add_all(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

print(add_all(1, 1))
print(add_all(1, 1, 1, 1, 1))

def print_profile(**infos):
    for info, value in infos.items():
        print(f"{info}: {value}")

print_profile(name="Jethro", hobby="Sleeping")

# Checkpoint Challenge
def build_order(item, quantity=1, **extras):
    print(f"item: {item}")
    print(f"quantity: {quantity}")
    for extra, value in extras.items():
        print(f"{extra}: {value}")

build_order("Burger", size="king", cheese="true")
build_order("Burger", 2, size="queen", cheese="false", egg="true")