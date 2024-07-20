# 1. Create the data that translates morse code (for a complete table, search on Google)
morse_code_dict: dict[str, str] = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/'
}


# 2. Create a function that converts the text and returns it as morse code
def convert_to_morse(text: str) -> str:
    return ' '.join(morse_code_dict.get(char.upper(), '') for char in text)


# 3. Create a main entry point
def main() -> None:
    # 4. Get that sexy user input
    user_input: str = input('Enter text: ')
    output: str = convert_to_morse(user_input)

    # 5. Display the output in the console
    print(output)


# 6. Run the script
if __name__ == "__main__":
    main()

"""
Homework:
1. Edit the program so that it also works with symbols, you're going to have
to do some research online and edit the dictionary.
2. Create a function that can convert the morse code back into regular text.

"""
