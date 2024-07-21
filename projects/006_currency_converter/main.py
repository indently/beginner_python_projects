# Import necessary functionality
import json


# Load the rates from a JSON file
def load_rates(json_file: str) -> dict[str, dict]:
    with open(json_file, 'r') as file:
        return json.load(file)


def convert(amount: float, from_currency: str, to_currency: str, rates: dict[str, dict]) -> float:
    # Make sure the user input is lowered
    from_currency: str = from_currency.lower()
    to_currency: str = to_currency.lower()

    # Get the rates
    from_rate: float = rates[from_currency]['rate']
    to_rate: float = rates[to_currency]['rate']

    # Return the rates
    if from_currency == 'eur':
        return amount * to_rate
    else:
        return amount * (to_rate / from_rate)


def main():
    # Load the rates
    rates: dict[str, dict] = load_rates('rates.json')

    # Get the result
    result: float = convert(amount=100, from_currency='dkk', to_currency='sek', rates=rates)
    print(result)


# Run the script
if __name__ == '__main__':
    main()


"""
Homework:
1. Right now it works fine if you insert a rate that exists, but make it so that if the user
enters a rate that doesn't exist, the program tells them that the currency is invalid, then
show them a list of all the valid currency options
2. [Hard] Instead of loading the data from a local JSON file, try loading the data from an API. 
This task will require you to search online for a free API for currency exchange rates, and to make
a request to it so that you can load that data in this script. 

"""