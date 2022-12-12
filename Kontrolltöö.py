 #Welcome the user with a message
print("hello")

# Convert the word "hello" to Morse code
print(".--. . .-.. .-.. ---")

# Create a dictionary that maps each letter to its Morse code representation
morse_code = {
  'a': '.-',
  'b': '-...',
  'c': '-.-.',
  'd': '-..',
  'e': '.',
  'f': '..-.',
  'g': '--.',
  'h': '....',
  'i': '..',
  'j': '.---',
  'k': '-.-',
  'l': '.-..',
  'm': '--',
  'n': '-.',
  'o': '---',
  'p': '.--.',
  'q': '--.-',
  'r': '.-.',
  's': '...',
  't': '-',
  'u': '..-',
  'v': '...-',
  'w': '.--',
  'x': '-..-',
  'y': '-.--',
  'z': '--..'
}

# Create a variable to store the user's input
user_input = ""

# Keep asking the user for words until they just press enter
while user_input != "":
  # Ask the user for a word
  user_input = input("Enter a word: ")

  # Convert the word to lowercase
  user_input = user_input.lower()

  # Create a variable to store the converted word
  converted_word = ""

  # Convert each letter of the word to Morse code
  for letter in user_input:
    # Check if the letter is in the Morse code dictionary
    if letter in morse_code:
      # Add the Morse code representation of the letter to the converted word
      converted_word += morse_code[letter] + " "
    else:
      # If the letter is not in the dictionary, ignore it
      continue

  # Print the converted word
  print(converted_word)
