import requests


class CurrencyConverter:
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data["rates"]

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != "EUR":
            amount = amount / self.currencies[from_currency]

        amount = round(amount * self.currencies[to_currency], 4)
        return amount


user_text = input('Enter message: ')
from_currency = user_text[9:12]
to_currency = user_text[13:16]
amount = int(user_text[17:])
url = "https://api.exchangerate-api.com/v4/latest/EUR"
converter = CurrencyConverter(url)
print(converter.convert(from_currency, to_currency, amount))