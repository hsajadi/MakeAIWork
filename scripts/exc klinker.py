# Define the string “paard”
word = "Paard"

# Define the counter
counter = 0

# Loop over each letter in string:
for char in word:

    # Check if character is vowel:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        # If so then increment counter
        counter = counter + 1

# Print result
print(f"Paard contains {counter} vowels")