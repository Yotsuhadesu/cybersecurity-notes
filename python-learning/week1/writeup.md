# Learnings of the week:

## Variable Assignment and Reassignment 
- Variable Assignment
    - Syntax: variable_name = value
- Variable Reassignment 
    - Syntax: variable_name = value

## Data Structures
1. List 
    - an ordered collection of values
    - Syntax: list_name = ["this", "is", "a", "list", "of", "Strings"]
2. Set 
    - an unordered collection of values without duplicate
    - the duplicate of a value will be skipped in printing
    - Syntax: set_name = {1, 2, 3, 4, 5, 5}
3. Tuple 
    - an ordered and immutable collection of values 
    - Syntax: tuple_name = (1, 2, 3, 4, 5)
4. Dict 
    - an ordered collection of keys with their corresponding values
    - Syntax: dict_name = {"Name" : "Jethro", "Height" : 170}

## Loops
1. For Loop 
    - Best if the iteration count is known or looping through a list.
    - Syntax:
        
            for value in list:
                code statement(s)
2. While Loop
    - Loops when a condition is met
    - Syntax: 

            while (condition):
                code statement(s)
3. Range
    - Used for looping through numbers
    - Syntax:
            
            1. for number in range(end):
                code statement(s)
            2. for number in range(start, end (excluded)):
                code statement(s)
            3. for number in range(start, end (excluded), update statement):
                code statement(s)
4. List Comprehension
    - Used for filling up lists with values
    - Syntax:

            1. list_name = [value for value in value_source]
            2. list_name = [value for value in value_source if condition]

## Technicalities
- A variable can be reassigned with values of different datatypes.
- An indented code block or statement is expected after a colon.