# for loop and range()

# for loop attempt
# for(i = 0; i < 5; i++):
#    print(i)

# for loop syntax
for i in range(5): 
    print(i)
print()

# Question: How about decrement?

for i in range(2, 10):
    print(i)
print()

# Observation: range(start, end (not included))

for i in range(0, 10, 2):
    print(i)
print()

# Observation: range(start, end (not included), update statement)

# Attempt for answering my question about decrement
for i in range(0, -12, -2):
    print(i)
print()

# looping directly over a list
chess_pieces = ["king", "queen", "bishop", "knight", "rook", "pawn"]

for pieces in chess_pieces:
    print(pieces)
print()

# Question: How to print statements in a single line?
# Answer

for pieces in chess_pieces:
    print(pieces, end = " ")
print()

# while loops
count = 0
while (count < 5):
    print(count)
    count += 1
print()

# Observation: ++/-- doesn't exist in python

# f strings
name = "Jethro"
age = 19
print(f"My name is {name} and I am {age}")
print(f"Next year, I'll be {age + 1}")

# Java Comparison: the f is inside the parenthesis and the variables are inserted directly via braces enclosure

# loop first approach
squares = []
for i in range(5):
    squares.append(i ** 2)
print(squares)
# Observation: the ** symbol is exponentation

# list comprehension - one-liner
# parts [(what gets stored) for (variable) in (what you are looping over)]
evens = [i for i in range(2, 10, 2)]
print(evens)

upper_pieces = [pieces.upper() for pieces in chess_pieces]
print(upper_pieces)

# parts of comprehension list with if
# [what is being stored for variable in what you are looping over if condition]
long_pieces = [piece for piece in chess_pieces if len(piece) > 5]
print(long_pieces)

# challenge
egg_counts = [2, 0, 1, 3, 2, 0, 1] 

# print the number of eggs per day using a for loop with range
for i in range(7):
    print(f"Day  {i + 1} :  {egg_counts[i]} eggs")

# create a list of good days (eggs >= 2) using list comprehension
good_days = [count for count in egg_counts if count >= 2]
print(good_days)

# convert egg_counts into f-string labels using a comprehension list
day_labels = [f"{count} eggs" for count in egg_counts]
print(day_labels)

# using a while loop, count the eggs until it reaches 5 and print which day it stopped
count = 0
index = 0
while(count < 5 and index < len(egg_counts)):
    count += egg_counts[index]
    index += 1
print(f"Day {index}")

# convert egg_counts into f-string labels but only the good days using a comprehension list
day_labels = [f"{count} eggs" for count in egg_counts if count >= 2]
print(day_labels)