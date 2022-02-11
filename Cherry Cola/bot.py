##################################
#### Cherry cola(discord bot) ####
#### Developed by James Meyer ####
####         9/30/2021        ####
##################################

from inspect import _void
from lib2to3.pgen2 import token
from typing import Collection
import discord
import os
import random
from discord.ext import commands, tasks
from itertools import cycle
import time
import sys
import topSecretFile

comments = """ hi """
status = cycle(["Dont stop believin'", 'Lemon Haze', 'ACDC', 'Metalica', 'Ice Cube'])
client = commands.Bot(command_prefix = '^')
rand_Seconds = random.randint(2000, 4000)



# ONLINE messages / status initialization / error handling
@client.event
async def on_ready():
    change_song.start()
    await client.change_presence(status=discord.Status.idle)
    words = "Welcome to Cherry Cola.\nThese cogs are runnning:\n"
    for char in words:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.025)
# END ONLINE MESSAGE

# Function to change the status of the bot
@tasks.loop(seconds=rand_Seconds)
async def change_song():
    rand_Seconds = random.randint(20, 50)
    channel = client.get_channel(941512464355434496)
    x = next(status)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=x))
    await channel.send("\N{cherries}Cherry changed song to: "+x+"\N{cherries}")

    

# END changing song function  

# Handling incorrect commands
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed=discord.Embed(
        title="INCORRECT COMMAND\n\nUSE ^help",
            description="\n\nTO SEE A LIST OF COMMANDS",
            color=discord.Colour.random())
        embed.set_thumbnail(url="https://www.nicepng.com/png/full/396-3963961_red-exclamation-point-png-graphic-exclamation-point.png")
        await ctx.send(embed=embed)
# END incorrect command handling


###########################
#### BOT IS NOW ONLINE ####
###########################



# ** UPDATE FUNCTIONS WITHOUT TAKING BOT OFFLINE **
#    Requires the name of the cog as a parameter
#      unload - unloads a Cog
#      load   - loads a Cog
#      reload - unloads then loads a cog again (updates)
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
# END UPDATE FUNCTIONS


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


# OWNER BLOCK
@client.command(aliases = ['Owner'])
async def owner(ctx):
    embed=discord.Embed(
    title="Developed by James Meyer",
        url="https://jrom.portfoliobox.net/home",
        description="Welcome to my Discord Bot\n   Cherry\N{cherries}Cola",
        color=discord.Colour.random())
    embed.set_thumbnail(url="https://d2f8l4t0zpiyim.cloudfront.net/000_clients/482824/page/h800-482824vwFiVdKz.jpg")
    await ctx.send(embed=embed)
# END OWNER BLOCK


@client.command(aliases =['changesong', 'songname'])
async def changesongx(ctx, *, songname):
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=songname))
    embed=discord.Embed(
        title="New song:\n"+songname,
        description = "Song changed by:\n"+ctx.message.author.mention,
        color= discord.Colour.random()
    )
    await ctx.send(embed=embed)

TOKEN = topSecretFile.TOKEN
client.run(TOKEN)
