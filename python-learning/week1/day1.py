# Indentation, Variable Types, Assignment

# Python figures out the data type of the variable via its assigned value
x = "Jethro"
print(x)    # Jethro

# You can reassign the variable with a value of different data type
x = 5
print(x)    # 5

# Assigning several variables in a single line
a, b, c = 1, 2, 3
print(a, b, c) # use comma to separate variables

# if/else statement
if (x > 0): # indentation on the next line is expected after a colon, grouping statements in a single code block
    print("x is a positive number")
elif (x < 0):
    print("x is a negative number")
else:
    print("x is zero")

# Checkpoint Challenge
name = "Jethro" # string
age = 18    # integer
is_stduent = True   # boolean - True or False
age = 19    # variable reasssignment
if (is_stduent):
    print(name, "is a student") # concatenate strings via comma
else:
    print(name, "is not a student")
