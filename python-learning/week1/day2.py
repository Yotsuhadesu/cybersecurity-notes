# Lists
characters = ["Keqing", "Neuvillette", "Nahida", "Columbina"]
print(characters[0])    # Access "Keqing" from the chracters list
print(characters[0:4])  # print the values stored in the list [starting index:stopping index (not included)]
characters.append("Ineffa") # Adding a value at the end
characters.append("Furina")
characters.remove("Ineffa") # Remove by value
print(characters)

# Observations:
# The list is dynamic and resizable

# Dict
friends_ar = {"Knx": 35, "DejaVu": 60, "bread": 60}
print(friends_ar["bread"])
print(friends_ar.get("Yotsuha"))    # Use .get to avoid crashing the program in accessing values
print(friends_ar.get("Yotsuha", 56))   
print(friends_ar)

# Tuple - unchangeable list
ages = (19.5, 20.7)
# ages[0] = 20.0 - Will result in an error

# Sets
numbers = {1, 2, 3, 4, 5, 5}
print(numbers)  # Only shows one of the value with duplicate

# Party Roster Tracker
roster = {"Neuvillette": "DPS", "Sucrose": "Support", "Columbina": "Sub-DPS"}
roster["Ineffa"] = "Sub-DPS"    # Add key and value to the roster dict
roster.pop("Sucrose")   # Safely remove Sucrose from the roster
sub_dps = ["Columbina", "Ineffa"]
tuple_sub_dps = tuple(sub_dps)
elements_used = {"hydro", "anemo", "hydro", "electro"}
print(elements_used)    # Will not print hydro two times
roster["Ineffa"] = "Shielder"   # Overwrites the value
print(roster)