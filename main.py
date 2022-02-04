import discord
import os
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
    if message.author == client.user:
        return

    elif message.content.startswith("!hello") or message.content.startswith("/hello"):
        await message.channel.send("/tts hello from a robot!")


client.run(TOKEN)