# 1. Import necessary functionality
import json


# 2. Load the rates from a JSON file
def load_rates(json_file: str) -> dict[str, dict]:
    with open(json_file, 'r') as file:
        return json.load(file)


# 3. Create the function
def convert(amount: float, base: str, to: str, rates: dict[str, dict]) -> float:
    # 4. Make sure the user input is lowered
    base = base.lower()
    to = to.lower()

    # 5. Get the dictionaries
    from_rates: dict | None = rates.get(base)
    to_rates: dict | None = rates.get(to)

    # 6. Return the rates
    if base == 'eur':
        return amount * to_rates['rate']  # type: ignore
    else:
        return amount * (to_rates['rate'] / from_rates['rate'])  # type: ignore


# 7. Create a main entry point
def main() -> None:
    # 8. Load the rates
    rates: dict[str, dict] = load_rates('rates.json')

    # 9. Get the result
    result: float = convert(amount=75, base='eur', to='dkk', rates=rates)
    print(result)


# 10. Run the script
if __name__ == '__main__':
    main()

"""
Homework:
1. Right now it works fine if you insert a rate that exists, but make it so that if the user
enters a rate that doesn't exist, the program tells them that the currency is invalid, then
show them a list of all the valid currency options.
2. Edit the script so that the "to" currency can also be specified as euro. 
3. [Hard] Instead of loading the data from a local JSON file, try loading the data from an API. 
This task will require you to search online for a free API for currency exchange rates, and to make
a request to it so that you can load that data in this script. 

"""
