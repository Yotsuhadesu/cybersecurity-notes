# Create a sentence or a paragraph as a string
sentence = "This is a sentence. You are looking at a sentence. I hope this sentence has meaning."

# Remove punctuation marks
clean_sentence = ""
for char in sentence:   # loop through all the characters in the sentence
    if char.isalnum() or char == " ":   # check if the current character is a letter, number, or a space 
        clean_sentence += char  # concatenate the character to the allocated string variable

# Split individual words from the string.
word_list = clean_sentence.split()
# .split() - splits the string into words and puts them in a list

# Track word counts
word_count = {} # create an empty dict
for word in word_list:
    word_count[word.lower()] = word_count.get(word.lower(), 0) + 1
    # .get(key, value) - safely finds a value, it returns the value if it exists and returns none if not
    # .lower() - toggles strings with uppercase letter(s) to all lowercase

# Track most common word
high_count = 0
common_word = ""
for word in word_count:
    if word_count.get(word) > high_count:
        high_count = word_count.get(word)
        common_word = word

# Print the result
print(f"Most common word: '{common_word}' {high_count} times")