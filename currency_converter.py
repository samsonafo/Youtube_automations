import requests

def currency_converter(amount, from_currency, to_currency):

    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)

    data = response.json()

    #fetch the rate for the target currency
    rate = data['rates'].get(to_currency)

    #convert the amount
    converted_amount = amount*rate
    return converted_amount, rate


if __name__ == "__main__":
    #example
    amount = 100
    from_currency = 'EUR'
    to_currency = 'NGN'

    converted_amount, rate = currency_converter(amount, from_currency, to_currency)

    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency} at an exchange rate of {rate:.4f}.")
