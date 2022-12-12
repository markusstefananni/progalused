# Greet the user with "hello" in normal language and Morse code
print("hello")
print(".-- .... .- .. ... .....")

# Create a dictionary mapping letters to their Morse code equivalents
morse_code_dict = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--.."
}

# Ask the user for words and convert them to Morse code
while True:
    word = input("Enter a word (or press Enter to quit): ")
    if word == "":
        break
    for letter in word:
        # Convert the letter to lowercase and look up its Morse code equivalent
        morse_code = morse_code_dict.get(letter.lower(), "")
        print(morse_code, end=" ")
    print()