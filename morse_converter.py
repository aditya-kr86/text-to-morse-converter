print("Welcome to the Text to Morse Code Converter!")
print("Note: Only letters (A-Z), numbers (0-9), and spaces are supported.\n")

# Morse code dictionary
morse_code_dict = {
    'A': ".-",     'B': "-...",   'C': "-.-.",   'D': "-..",    'E': ".",
    'F': "..-.",   'G': "--.",    'H': "....",   'I': "..",     'J': ".---",
    'K': "-.-",    'L': ".-..",   'M': "--",     'N': "-.",     'O': "---",
    'P': ".--.",   'Q': "--.-",   'R': ".-.",    'S': "...",    'T': "-",
    'U': "..-",    'V': "...-",   'W': ".--",    'X': "-..-",   'Y': "-.--",
    'Z': "--..", 
    '0': "-----",  '1': ".----",  '2': "..---",  '3': "...--",  '4': "....-",
    '5': ".....",  '6': "-....",  '7': "--...",  '8': "---..",  '9': "----.",
    ' ': "/"  # Add a separator for spaces
}

# Get user input
text = input("Enter the text you want to convert to Morse code: ").strip()

# Convert to Morse code
morse_code = ""
for character in text:
    if character.upper() in morse_code_dict:
        morse_code += morse_code_dict[character.upper()] + " "
    else:
        print(f"Warning: Character '{character}' cannot be converted to Morse code. Skipping.")

# Display result
if morse_code:
    print(f"\nThe Morse code for '{text}' is:\n{morse_code.strip()}")
else:
    print("Error: No valid text entered to convert!")
