# bot.py
import os

import discord
from dotenv import load_dotenv
import requests

load_dotenv()
TOKEN = os.getenv("TOKEN")
GUILD = os.getenv("GUILD")

client = discord.Client()


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


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f"{client.user} is connected to the following guild:\n"
        f"{guild.name} (id: {guild.id})"
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if '!convert' in message.content:
        to_convert = message.content
        from_currency = to_convert[9:12]
        to_currency = to_convert[13:16]
        amount = int(to_convert[17:])
        url = "https://api.exchangerate-api.com/v4/latest/EUR"
        converter = CurrencyConverter(url)
        response = (f"Converted amount is {converter.convert(from_currency.upper(), to_currency.upper(), amount)} "
                    f"{to_currency}")
        await message.channel.send(response)


client.run(TOKEN)
