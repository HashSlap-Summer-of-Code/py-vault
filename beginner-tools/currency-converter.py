# beginner-tools/currency-converter.py

"""
Currency Converter CLI Tool

Usage:
    python currency-converter.py <amount> <from_currency> <to_currency>
Example:
    python currency-converter.py 100 USD EUR
"""

import sys
import requests

API_KEY = "8dc160711d0bd8f08b933609"  # Replace with your own key if needed

def get_exchange_rate(from_currency, to_currency):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Failed to fetch exchange rates.")

    data = response.json()

    if data["result"] != "success":
        raise Exception(f"API error: {data.get('error-type', 'Unknown error')}")

    rates = data["conversion_rates"]

    if to_currency not in rates:
        raise Exception(f"Currency {to_currency} not supported.")

    return rates[to_currency]

def convert_currency(amount, from_currency, to_currency):
    rate = get_exchange_rate(from_currency.upper(), to_currency.upper())
    return amount * rate

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python currency-converter.py <amount> <from_currency> <to_currency>")
        sys.exit(1)

    try:
        amount = float(sys.argv[1])
        from_currency = sys.argv[2]
        to_currency = sys.argv[3]

        result = convert_currency(amount, from_currency, to_currency)
        print(f"{amount} {from_currency.upper()} = {result:.2f} {to_currency.upper()}")

    except ValueError:
        print("Please enter a valid number for the amount.")
    except Exception as e:
        print(f"Error: {e}")