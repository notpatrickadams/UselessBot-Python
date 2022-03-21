import discord, os, logging
from dotenv import load_dotenv

from functions.bee import generate_random
from functions.pokemon import get_pokemon

client = discord.Client()
load_dotenv()
logging.basicConfig(filename="bot.log", format="%(asctime)s - %(message)s", level=logging.INFO)

@client.event
async def on_ready():
    print("[i] Bot started!")
    logging.info(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith("!bee"):
        logging.info(f"Bee requested by { message.author.mention }")
        filename = generate_random()
        await message.channel.send("Here's your bee!", file=discord.File(fp=filename, filename="image.png"))
        logging.info("Bee successfully generated and sent")
    elif "lamp" in message.content.lower():
        logging.info(f"Sent moth image to { message.author.mention }")
        await message.channel.send("Moth summoned.", file=discord.File(fp="moth.jpg"))
    elif message.content.startswith("!pokemon"):
        logging.info(f"Pokemon requested by { message.author.mention }")
        pkmn = get_pokemon()
        emb = discord.Embed(title=pkmn["name"], description=pkmn["genus"], thumbnail=pkmn["icon"], color=0xDDDDDD)
        emb.set_image(url=pkmn["icon"])
        emb.add_field(name="Dex Number", value=pkmn["dex_no"], inline=False)
        emb.add_field(name="Flavor text", value=pkmn["flavor_text"], inline=False)
        emb.add_field(name="Types", value=", ".join(pkmn["types"]), inline=False)
        await message.channel.send(embed=emb)
        logging.info(f"Pokemon: {pkmn['name']} #{pkmn['dex_no']} sent")


client.run(os.getenv("DISCORD_TOKEN"))