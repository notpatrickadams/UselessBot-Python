import os, logging, json
from dotenv import load_dotenv

import interactions
from interactions.ext.files import command_send

from functions.bee import generate_random
from functions.magic7 import magic7_generate
from functions.idea_generator import idea_generator
from functions.rice_price import rice_price
from functions.urban_dictionary import urban_dictionary

load_dotenv()
logging.basicConfig(filename="bot.log", format="%(asctime)s - %(message)s", level=logging.INFO)

bot = interactions.Client(token=os.getenv("DISCORD_TOKEN"), intents=interactions.Intents.DEFAULT | interactions.Intents.GUILD_MESSAGE_CONTENT)
bot.load("interactions.ext.files")

# Loads IDs of clowns
try:
    with open("config/clowns.json") as f:
        CLOWNS = json.loads(f.read())["ids"]
except FileNotFoundError:
    logging.info("No clowns found... Creating them...")
    if not os.path.exists("config/"):
        os.mkdir("config/")
    with open("config/clowns.json", "w") as f:
        f.write(
            """
            {
                "ids": [
                    "INSERT CLOWNS AS A STRING HERE"
                ]
            }
            """
        )

@bot.event
async def on_ready():
    print("[i] Bot started!")
    logging.info(f"Logged in as { bot.me.name }")

@bot.command(name="bee", description="Sends a bee!")
async def bee(ctx: interactions.CommandContext):
    logging.info(f"Bee requested by { ctx.author }")
    filename = generate_random()
    f = interactions.File(filename="image.png", fp=filename)
    await command_send(ctx, "Here's your bee!", files=f)
    logging.info("Bee successfully generated and sent")

@bot.command(name="magic7", description="Ask the Magic 7 Ball a question!", options=[
        interactions.Option(
            name="inquiry", 
            description="What you want to ask the Magic 7 Ball", 
            type=interactions.OptionType.STRING,
            required=True
        )
    ])
async def magic7(ctx: interactions.CommandContext, inquiry: str):
    logging.info(f"Providing life advice to { ctx.author } with question: { inquiry }")
    await ctx.send(f"You asked: { inquiry }\nA: " + magic7_generate())

@bot.command(name="idea", description="Generate a random startup idea!")
async def idea(ctx: interactions.CommandContext):
    logging.info(f"Random idea requested by { ctx.author }")
    await ctx.send(idea_generator())

@bot.command(name="hi", description="The bot will mention you")
async def hi(ctx: interactions.CommandContext):
    logging.info(f"Mentioning { ctx.author }")
    await ctx.send(f"Hi { ctx.author.mention }")

@bot.command(name="rice", description="Gets the last price of rice per pound")
async def rice(ctx: interactions.CommandContext):
    logging.info(f"{ ctx.author } is requesting the price of rice")
    try:
        rice = await rice_price()
        if rice != 0:
            await ctx.send(f"The price of rice is ${ rice / 100 } USD per pound")
        else:
            await ctx.send("Rice is not available at the moment.", ephemeral=True)
    except Exception as e:
        logging.info(e)
        await ctx.send("Broken whoops", ephemeral=True)

@bot.command(name="ud", description="Gets the definition of a term on Urban Dictionary", options=[
        interactions.Option(
            name="term",
            description="Term to search on Urban Dictionary",
            type=interactions.OptionType.STRING,
            required=True
        )
    ])
async def ud(ctx: interactions.CommandContext, term: str):
    logging.info(f"{ ctx.author } looked up { term }")
    try:
        res = await urban_dictionary(term)
        if len(res) == 0:
            await ctx.send(f"""Couldn't find "{ term }" on Urban Dictionary""", ephemeral=True)
            return
        first_res = res[0]
        embed = interactions.Embed(title=first_res['word'].capitalize(), url=first_res['permalink'])
        if len(first_res["definition"]) > 1000:
            first_res["definition"] = first_res["definition"][:1000] + "..."
        embed.add_field("Definition", first_res["definition"])
        await ctx.send(embeds=embed)
    except Exception as e:
        logging.error(e)

@bot.event
async def on_message_create(message: interactions.Message):
    if message.author == bot.me.name:
        return
    elif "lamp" in message.content.lower():
        logging.info(f"Reacting with moth to { message.author.mention }")
        await message.create_reaction(r":moth:1011626571930542202")
    elif "sus" in message.content.lower():
        logging.info(f"Reacting with :sus: on message by { message.author.mention }")
        await message.create_reaction(r":sus:1011595741631885342")
    elif message.author.mention[2:-1] in CLOWNS:
        logging.info(f"Reacting with clown")
        await message.create_reaction(r"🤡")

bot.start()