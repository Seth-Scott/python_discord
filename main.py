import discord
import os
import time
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TOKEN")


client = discord.Client()
print("Starting Discord bot..")
print(f"VERSION: {discord.__version__}")


@client.event
async def on_ready():
    print("{0.user} is online!".format(client))


@client.event
async def on_message(message):
    # prints username, time and message to terminal for debug
    print(f"{message.author} {time.strftime('%H:%M:%S')}: {message.content}")

    if message.author == client.user:
        return

    elif message.content.startswith("/hello"):
        await message.channel.send("hello!")


client.run(TOKEN)