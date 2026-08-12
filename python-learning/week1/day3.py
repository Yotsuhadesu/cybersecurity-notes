# For Loops, While Loops, range()

# For Loop - traverses through the items in something like lists, dicts, and etc.
"""
Syntax:
for [item] in [lists, range, etc.]
"""
names = ["Ace", "Rover", "Cydrex"]
for name in names:
    print(name)

# range() - when you need to loop through a specific number range
"""
Syntax: 
1. range(end (0 is the start and the end is not included))
2. range(start, end (not included))
3. range(start, end (not included), update statement)
"""
for number in range(1):
    print(number)

# While Loop - loops if the condition is met
"""
Syntax: 
while (condition):
    indented code block/sentence
"""
i = 0
while (i < 5):
    print(i)
    i += 1  # update statement

# Mini Challenges
# range()
for i in range(0, 10):
    print(i)
for i in range(10, 0, -1):
    print(i)

# For Loop
list = ["this", "is", "a", "list"]
for word in list:
    print(word)

# While Loop
i = 5
while (i > 0):
    print(i)
    i -= 1

# Checkpoint Challenge
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []
for number in numbers:
    if (number % 2 == 0):
        even_numbers.append(number)
print(even_numbers)

sum = 0
counter = 0
index = 0
while (sum <= 50):
    sum += even_numbers[index]
    index += 1
    if (index == len(even_numbers)): 
        index = 0
    counter += 1
print(sum, counter)

even_squares = {}
for number in even_numbers:
    even_squares[number] = number * number
print(even_squares)