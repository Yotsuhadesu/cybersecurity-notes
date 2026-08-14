# Create a sentence or a paragraph as a string
sentence = "This is a sentence. You are looking at a sentence."

# Split individual words from the string.
word_list = sentence.split()
# .split() - splits the string into words and puts them in a list

# Track word counts
word_count = {} # create an empty dict
for word in word_list:
    word_count[word] = word_count.get(word.lower(), 0) + 1
    # .get(key, value) - safely finds a value, it returns the value if it exists and returns none if not

# Track most common word
high_count = 0
common_word = ""
for word in word_count:
    if word_count.get(word) > high_count:
        high_count = word_count.get(word)
        common_word = word

# Print the result
print(f"Most common word: '{word}' {high_count} times")