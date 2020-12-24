import os
import discord
import requests
from dotenv import load_dotenv
# environment init
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
WEATHER_LOCATION = os.getenv("WEATHER_LOCATION")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
# discord init
bot = discord.Client()
# weather init
URL = f"http://api.openweathermap.org/data/2.5/weather?q={WEATHER_LOCATION}&appid={WEATHER_API_KEY}"


kelvin = -273.15

@bot.event
async def on_ready():
    print("bot is live.")

@bot.event
async def on_message(message):
    if message.content.startswith('!silivribot'):
        # SENDS BACK A MESSAGE TO THE CHANNEL.
        res = requests.get(url=URL)
        temp = res.json()['main']['temp'] + kelvin
        tempstring = "{:.1f}".format(temp)
        if (temp > 0 and temp < 15):
            await message.channel.send("Silivri'de hava şu an {} °C ve hakikaten soğuk.".format(tempstring))
        elif (temp < 0):
            await message.channel.send("Silivri'de hava şu an {} °C ve cidden soğuk.".format(tempstring))
        else:
            await message.channel.send(str("Silivri'de hava şu an {} °C ve soğuk değil malesef.", 'utf-8').format(tempstring))



    # EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.

bot.run(DISCORD_TOKEN)