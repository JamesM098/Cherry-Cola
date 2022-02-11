######################
#### runescape.py ####
######################

import discord
import asyncio
import json
from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import time
import sys

class Runescape(commands.Cog):
    def __init__(self, client):
        self.client = client

##################
#### events   ####
##################

    @commands.Cog.listener()
    async def on_ready(self):
        # Every "Current Cog", CC, will be written to the console so the running cogs are known at boot up  
        words = "  CC - Runescape\n"
        for char in words:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)

##################
#### commands ####
##################


    # Function to return some statistics about a certain player on RuneScape
    # The players name is entered into the URL
    # Using BeautifulSoup, some data is extracted
    @commands.command()
    async def stats(self, ctx, *, player_name):
        
        # URL of the json file provided by RuneScape API
        source = requests.get('https://apps.runescape.com/runemetrics/profile/profile?user='+player_name).text
        soup = BeautifulSoup(source, 'lxml')
        script = soup.find_all('body')[0].text
        data = json.loads(script)
        tskill = data['totalskill']
        totalXP = data['totalxp']

        # dont remember why I have this formatted like this
        # FINDOUT WHY
        recentActivity = data['activities'][0]['details']
        

        # Creating the card to be displayed on discord with all of the information
        cPlayer_name = player_name.capitalize()
        embed=discord.Embed(
        title= 'LINK TO HiSCORES',
            url="https://apps.runescape.com/runemetrics/app/overview/player/"+player_name,
            description="   Hiscore Stats for "+cPlayer_name,
            color= discord.Color.blue())
        embed.set_author(name=cPlayer_name, icon_url="https://secure.runescape.com/m=avatar-rs/"+player_name+"/chat.png")
        embed.set_thumbnail(url="https://secure.runescape.com/m=avatar-rs/"+player_name+"/chat.png")
        embed.add_field(name="**Total Level**", value=tskill, inline=False)
        embed.add_field(name="**Total XP**", value=totalXP, inline=False)
        embed.add_field(name="**Recent Activity**", value=recentActivity, inline=False)
        await ctx.send(embed=embed)


    # This function just returns a link to a reference page for RuneScape
    @commands.command()
    async def skill(self, ctx, *, skill_name):

            if skill_name == "list":
                embed=discord.Embed(
                title="List of skills: \n",
                    url="https://runescape.wiki/w/Skills",
                    description='Agility, Archaeology, Attack, Cooking, Constitution\nConstruction, Crafting, Defence, Divination, Dungeoneering\n'+
                          'Farming, Fishing, Firemaking, Fletching, Herblore, Hunter\nInvention, Magic, Mining, Prayer, Ranged\n Runecrafting, '+
                          'Slayer, Smithing, Strength, Summoning, Thieving, Woodcutting',
                    color= discord.Color.random())
                embed.set_thumbnail(url="https://icons.iconarchive.com/icons/papirus-team/papirus-apps/256/runescape-icon.png")
                async with ctx.typing():
                    await asyncio.sleep(1)
                await ctx.send(embed=embed)

            else:
                cSkill_name = skill_name.capitalize()
                embed=discord.Embed(
                title=cSkill_name,
                    url="https://runescape.wiki/w/"+skill_name,
                    description="CLICK THE LINK ABOVE",
                    color= discord.Color.random())
                embed.set_thumbnail(url="https://www.runescape.com/img/rs3/hiscores/large-icon-"+skill_name+".png")
                async with ctx.typing():
                    await asyncio.sleep(1)
                await ctx.send(embed=embed)


    @commands.command()
    async def wiki(self, ctx, *, search_name):

            cSkill_name = search_name.capitalize()
            embed=discord.Embed(
            title="CLICK HERE FOR THE LINK",
                url="https://runescape.wiki/w/"+cSkill_name,
                color= discord.Color.random())
            embed.set_author(name="Wiki link Below", icon_url="https://pbs.twimg.com/profile_images/1080165853499441152/XVrTFNbN.jpg")
            embed.set_image(url="https://media1.tenor.com/images/4a487015765accefb1d2ca814fda4001/tenor.gif?itemid=13112699")
            async with ctx.typing():
                await asyncio.sleep(1)
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Runescape(client))
