# 1. Import necessary functionality
import secrets
import string


# 2. Create a class
class Password:
    # 3. Initialize our class
    def __init__(self, length: int = 12, uppercase: bool = True, symbols: bool = True) -> None:
        self.length = length
        self.use_uppercase = uppercase
        self.use_symbols = symbols

        # 4. Get characters from the string module
        self.base_characters: str = string.ascii_lowercase + string.digits

        # 5. Add symbols and uppercases characters if the user wants them
        if self.use_uppercase:
            self.base_characters += string.ascii_uppercase
        if self.use_symbols:
            self.base_characters += string.punctuation

    # 6. Create a method to generate the password
    def generate(self) -> str:
        password: list[str] = []

        for i in range(self.length):
            password.append(secrets.choice(self.base_characters))

        return ''.join(password)


# 7. Create the main entry point
def main() -> None:
    password: Password = Password(length=20, uppercase=True, symbols=True)
    for i in range(10):
        generated: str = password.generate()
        print(f'{generated} ({len(generated)} chars)')


# 8. Run the script
if __name__ == '__main__':
    main()

"""
Homework:
1. Create a method in the Password class which checks the passwords strength. 
- check that the password is more than 16 characters long
- check that the password both contains uppercase characters and symbols

"""
