import discord, os, logging
from bee import generate_random

client = discord.Client()
logging.basicConfig(filename="bot.log", format="%(asctime)s - %(message)s", level=logging.INFO)

@client.event
async def on_ready():
    logging.info(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith("!bee"):
        logging.info(f"Bee requested by {message.author.mention}")
        filename = generate_random()
        with open(filename, 'rb') as f:
            file_to_send = discord.File(f, filename=filename)
        await message.channel.send("Here's your bee!", file=file_to_send)
        logging.info("Bee successfully generated and sent")

client.run(os.getenv("DISCORD_TOKEN"))