from forex_python.converter import CurrencyRates

def convert_currency(amount, from_currency, to_currency):
    cr = CurrencyRates()
    converted_amount = cr.convert(from_currency, to_currency, amount)
    return converted_amount

amount = float(input("Enter amount: "))
from_currency = input("From currency (e.g., USD): ")
to_currency = input("To currency (e.g., EUR): ")

print(f"{amount} {from_currency} is equal to {convert_currency(amount, from_currency, to_currency)} {to_currency}")
