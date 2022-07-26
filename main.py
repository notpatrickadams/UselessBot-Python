import os, logging
from dotenv import load_dotenv

from discord import Intents, File
from discord.ext.commands import Bot
from discord_slash import SlashCommand

from functions.bee import generate_random
from functions.magic7 import magic7_generate
from functions.idea_generator import idea_generator
from functions.rice_price import rice_price

bot = Bot(command_prefix="!", self_bot=True, help_command=None, intents=Intents.default())
slash = SlashCommand(bot, sync_commands=True)

load_dotenv()
logging.basicConfig(filename="bot.log", format="%(asctime)s - %(message)s", level=logging.INFO)

@bot.event
async def on_ready():
    print("[i] Bot started!")
    logging.info(f"Logged in as {bot.user}")

@slash.slash(description="Sends a bee!")
async def bee(ctx):
    logging.info(f"Bee requested by { ctx.author }")
    filename = generate_random()
    await ctx.send("Here's your bee!", file=File(fp=filename, filename="image.png"))
    logging.info("Bee successfully generated and sent")

@slash.slash(description="Ask the Magic 7 Ball a question!")
async def magic7(ctx, inquiry):
    logging.info(f"Providing life advice to { ctx.author } with question: { inquiry }")
    await ctx.send(f"You asked: { inquiry }\nA: " + magic7_generate())

@slash.slash(description="Generate a random startup idea!")
async def idea(ctx):
    logging.info(f"Random idea requested by { ctx.author }")
    await ctx.send(idea_generator())

@slash.slash(description="The bot will mention you")
async def hi(ctx):
    logging.info(f"Mentioning { ctx.author }")
    await ctx.send(f"Hi { ctx.author.mention }")

@slash.slash(description="Gets the last price of rice per pound")
async def rice(ctx):
    logging.info(f"{ ctx.author } is requesting the price of rice")
    await ctx.send(f"The price of rice is ${ rice_price() / 100 } USD per pound")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    elif "lamp" in message.content.lower():
        logging.info(f"Sent moth image to { message.author.mention }")
        await message.channel.send("Moth summoned.", file=File(fp="moth.jpg"))

bot.run(os.getenv("DISCORD_TOKEN"))