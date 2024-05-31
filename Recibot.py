import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f"hemos iniciado con el bot {bot.user}")

#manualidades con plastico
@bot.command()
async def manualidades(ctx):
    ideas=["realizar ladrillos ecologicos",
           "crear una lampara con cucharas de plastico.",
           "crear un adorno navideño con tapas de plastico.", 
           "realizar una silla recicladora"]
    await ctx.send(random.choice(ideas))

#clasificacion de residuos
@bot.command()
async def clasificacion(ctx,*,item:str):
    reciclables=["botella de plastico", "papel", "lata", "mascarilla de plastico"]
    no_reciclable=["pañales","comida", "agua"]

    if item.lower() in reciclables:
        await ctx.send("puede ser reciclado")
    elif item.lower() in no_reciclable:
        await ctx.send("no puede ser reciclado")
    else:
        await ctx.send("no tengo conocimiento de eso")
bot.run("")
