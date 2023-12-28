# Saving a long sentence as a single string in a variable:
long_sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# Printing out the sentence with spaces in replacement of the exclamation marks:
print(long_sentence.replace("!"," "))

# Printing out the same sentence again, with spaces and all uppercase letters:
print(long_sentence.replace("!"," ").upper())

# Printing out the original sentence on reverse order:
print(long_sentence[::-1])

# As a plus, printing out the sentence on reverse order, with spaces in replacement of the exclamation marks:
print(long_sentence.replace("!"," ")[::-1])

