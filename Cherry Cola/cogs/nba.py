################
#### nba.py ####
################


# Wanting to scrape google to find a random picture of the NBA and have it printed
# on a card within discord once the command ^NBA is called
#                                           ^nba

import discord
import random
from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import time
import sys

class NBA(commands.Cog):

    def __init__(self, client):
        self.client = client


    #events
    @commands.Cog.listener()
    async def on_ready(self):
        words = "  CC - NBA\n"
        for char in words:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)


    @commands.command()
    async def woot(self, ctx):
        await ctx.send('GO THE PELICANS')

    @commands.command()
    async def nbapic(self, ctx):

        URL = "https://www.google.com/search?q=NBA&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjv44CC_sXwAhUZyjgGHSgdAQ8Q_AUoAXoECAEQAw&cshid=1620885828054361"
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')
        image_tags = soup.find_all('img', class_='yWs4tf')
        links = []
        for image_tag in image_tags:
            links.append(image_tag['src'])
        
        link = random.choice(links)

        # Debugging to see how many links are appended to the array of links
        print(len(links))
        embed=discord.Embed(
            title= 'NBA PICTURE',
                url="https://NBA.com",
                description="   Pictures of NBA",
                color= discord.Color.blue())

        embed.set_image(url = link)
        await ctx.send(embed=embed)
        

def setup(client):
    client.add_cog(NBA(client))
