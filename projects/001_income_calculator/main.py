# 1. Create a function to calculate finances
def calculate_finances(monthly_income: float, tax_rate: float, currency: str) -> None:
    # 2. Do the math for each field
    yearly_salary: float = monthly_income * 12
    monthly_tax: float = monthly_income * (tax_rate / 100)
    yearly_tax: float = monthly_tax * 12
    monthly_net_income: float = monthly_income - monthly_tax
    yearly_net_income: float = yearly_salary - yearly_tax

    # 3. Format the information nicely for the user
    print('--------------------------------')
    print(f'Monthly income: {currency}{monthly_income:,.2f}')
    print(f'Tax rate: {tax_rate:,.0f}%')
    print(f'Monthly tax: {currency}{monthly_tax:,.2f}')
    print(f'Monthly net income: {currency}{monthly_net_income:,.2f}')
    print(f'Yearly salary: {currency}{yearly_salary:,.2f}')
    print(f'Yearly tax paid: {currency}{yearly_tax:,.2f}')
    print(f'Yearly net income: {currency}{yearly_net_income:,.2f}')
    print('--------------------------------')


# 4. Create a main entry point for the program
def main() -> None:
    # 5. Gather user input
    monthly_income: float = float(input('Enter your monthly income: '))
    tax_rate: float = float(input('Enter your tax rate (%): '))

    # 6. Call the function
    calculate_finances(monthly_income, tax_rate, currency='KR')


# 7. Run the script
if __name__ == "__main__":
    main()

"""
Homework:
1. Edit the script so that users can also enter their expenses (eg. rent, food, gym memberships) so they
can see how much they have left over each month.
2. Recreate the user input section to safely handle users inserting the wrong type without 
crashing the program.

"""
