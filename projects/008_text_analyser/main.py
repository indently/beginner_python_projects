# 1. Create a function that handles opening files
def open_file(path: str) -> str:
    with open(path, 'r') as file:
        text: str = file.read()
        return text


# 2. Create a function that analyses any string
def analyse(text: str) -> dict[str, int]:
    result: dict[str, int] = {
        'total_chars_incl_spaces': len(text),
        'total_chars_excl_spaces': len(text.replace(' ', '')),
        'total_spaces': text.count(' '),
        'total_words': len(text.split())
    }

    return result


# 3. Create a main entry point
def main() -> None:
    text: str = open_file(path='note.txt')
    analysis: dict[str, int] = analyse(text)

    # 4. Display the information
    for key, value in analysis.items():
        print(f'{key}: {value}')


# 5. Run the script
if __name__ == '__main__':
    main()


"""
Homework:
1. Create a much more user friendly message regarding the analysis (eg. "This text file contains...").
2. Add the top 5 most common words to the analysis message.

"""