# Define an input string
chosen_string = "happy new year to all of you!"

# Alternatively, comment the above code and use this, reading an input string from the user
# chosen_string = input("Enter a string: ")

# Make each alternate character uppercase and lowercase
alternate_characters = ''
for i, char in enumerate(chosen_string):
    if i % 2 == 0:
        alternate_characters += char.upper()
    else:
        alternate_characters += char.lower()

# Print the result for the alternate characters
print(f"(Alternate characters) {alternate_characters}")

# Make each alternate word lowercase and uppercase
words = chosen_string.split()
alternate_words = []
for i, word in enumerate(words):
    if i % 2 == 0:
        alternate_words.append(word.lower())
    else:
        alternate_words.append(word.upper())

# Join the words back into a string and print the result for the alternate words
alternate_words_string = ' '.join(alternate_words)
print(f"(Alternate words) {alternate_words_string}")
