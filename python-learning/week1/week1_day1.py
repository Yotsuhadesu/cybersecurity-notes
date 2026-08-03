# Python variable assignment and reassignment and its Java equivalent
name = "Jethro"
# String name = "Jethro";
age = 19
# int age = 19;
age = "hi"
# String age = "hi";    // different variable error
age = 'a'
# char age = 'a';   // different variable error
age = 19.9
# double age = 19.9;    // different variable error
print(name, age)
# System.out.println(name + " " + age)

# Observations
# Python doesn't need semicolons to break lines.
# The value itself is the datatype.
# The complier doesn't complain when I reassign values of different types on a variable.
# To comment, use hashtag.
# Printing concatenation only needs comma.
# Values enclosed in '' or "" are treated as string.
# Numbers with decimals are treated as float

x = 6
y = 5
if (x > y):
    print("x is greater than y")
    print("y is less than x")
elif (y > x): print("y is greater than x")
else:
    print("y and x is equal")

# Java equivalent
# if (x > y) {
#   System.out.println("x is greater than y");
#   System.out.println("y is less than x");
# } else if (y > x)
#   System.out.println("y is greater than x");
# else {
#   System.out.println("x and y is equal")
# }

# Observations:
# Lines on the same indentation are treated as block
# You can put the line to be executed on the same line as the condition
# A colon is a signal that an indentation is to be expected after the line.