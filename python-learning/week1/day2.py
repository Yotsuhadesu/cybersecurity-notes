# Data Structures, f-strings, List Comprehensions

# Four core containers for holding values
# 1. List - ordered collection of values
list = ["this", "is", "a", "list"]
print(list)

# 2. Dict - a collection of keys and their corresponding value
dict = {"d":0, "i":1, "c":2, "t":3}
print(dict)

# Tuple - ordered set that can't be changed
tuple = (1, 2, 3, 4, 5)
print(tuple)

# Set - unordered collection with no duplicates
set = {"s", "e", "e", "t"}
print(set)

# f-strings - let you insert a variable directly into a sentence
name = "Jethro"
print(f"Hello, my name is {name}")

# List Comprehension - shortcut for building lists
list_copy = [value for value in list]
print(list_copy)

# Mini Challenges
list = [1, 2, 2, 3, 4]
tuple = (1, 2, 2, 3, 4)
set = {1, 2, 2, 3, 4}
print(list)
print(tuple)
print(set)  # prints the set with no duplicate 2

dict = {"apple": 25, "banana": 15, "orange": 20}
print(dict.get("apple"))
dict["grape"] = 1
print(dict) 

a = 2
b = 3
print(f"Total: {a + b}")

# List Comprehension Drills
squares = []
for number in range(1, 11):
    squares.append(number * number)
print(squares)

squares = [number * number for number in range(1, 11)]
print(squares)

even_numbers = []
for number in range(1, 21):
    if (number % 2 == 0):
        even_numbers.append(number)
print(even_numbers)

even_numbers = [number for number in range(1, 21) if number % 2 == 0]
print(even_numbers)

list = ["lower", "case"]
uppercase = []
for word in list:
    uppercase.append(word.upper())
print(uppercase)

uppercase = [word.upper() for word in list]
print(uppercase)

length = []
for word in list:
    length.append(len(word))
print(length)

length = [len(word) for word in list]
print(length)

first_letter = []
for word in list:
    first_letter.append(word[0])
print(first_letter)

first_letter = [word[0] for word in list]
print(first_letter)

# Checkpoint Challenge
question = ["Should", "I", "pull", "for", "Odette", "or", "wait", "for", "Furina?"]

length_uppercase = [word.upper() for word in question if len(word) > 4]
print(length_uppercase)

length = {word: len(word) for word in question}
print(length)