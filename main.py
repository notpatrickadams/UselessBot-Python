import discord, os, logging
from bee import generate_random
from dotenv import load_dotenv

client = discord.Client()
load_dotenv()
logging.basicConfig(filename="bot.log", format="%(asctime)s - %(message)s", level=logging.INFO)

@client.event
async def on_ready():
    logging.info(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith("!bee"):
        logging.info(f"Bee requested by { message.author.mention }")
        filename = generate_random()
        with open(filename, 'rb') as f:
            file_to_send = discord.File(f, filename=filename)
        await message.channel.send("Here's your bee!", file=file_to_send)
        logging.info("Bee successfully generated and sent")
    elif "lamp" in message.content.lower():
        logging.info(f"Sent moth image to { message.author.mention }")
        await message.channel.send("Moth summoned.", file=discord.File(fp="moth.jpg"))

client.run(os.getenv("DISCORD_TOKEN"))