# Import necessary functionality
import secrets
import string


# Create a class
class Password:
    # Initialize our class
    def __init__(self, length=12, uppercase=True, symbols=True):
        self.length = length
        self.use_uppercase = uppercase
        self.use_symbols = symbols

        # Get characters from the string module
        self.base_characters: str = string.ascii_lowercase + string.digits
        self.uppercase_letters: str = string.ascii_uppercase
        self.symbols: str = string.punctuation

        # Add symbols and uppercases characters if the user wants them
        if self.use_uppercase:
            self.base_characters += self.uppercase_letters
        if self.use_symbols:
            self.base_characters += self.symbols

    # Create a method to generate the password
    def generate(self):
        password: list[str] = []

        for i in range(self.length):
            password.append(secrets.choice(self.base_characters))

        return ''.join(password)


# Create the main entry point
def main() -> None:
    password: Password = Password(length=20, uppercase=True, symbols=True)
    for i in range(10):
        generated: str = password.generate()
        print(f'{generated} ({len(generated)} chars)')


# Run the script
if __name__ == '__main__':
    main()

"""
Homework:
1. Create a method in the Password class which checks the passwords strength. 
- check that the password is more than 16 characters long
- check that the password both contains uppercase characters and symbols

"""
