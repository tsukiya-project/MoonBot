import discord
import config

intents = discord.Intents.default()
intents.members = True
intents.messages = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.content.startswith("!hello"):
        await message.channel.send("Hello!")

client.run(config.TOKEN)
