##################
#### sammy.py ####
##################


import discord
import random
import asyncio
from discord.ext import commands
import time
import sys
import requests
from bs4 import BeautifulSoup

class Sammy(commands.Cog):

    def __init__(self, client):
        self.client = client


    #events
    @commands.Cog.listener()
    async def on_ready(self):

        # Every "Current Cog", CC, will be written to the console so the running cogs are known at boot up
        words = "  CC - Sammy\n"
        for char in words:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)

    #commands
    @commands.command()
    async def hello(self, ctx):
        await ctx.send(':wave:')

    @commands.command()
    async def goodbye(self, ctx):
        await ctx.send(':wave: BYE FOREVER :wave:')

    # Random function mainly tasting the 'aliases' part of commands within Discord API
    @commands.command(aliases =['godmonig','godmoiring','goodmroning','goodmirng','goodmronigng','goodmrongin', 'goodmornng', 'godmroming', 'godmorning', 'goodmorningg', 'goodmornuign!','godokmring', 'goodnmringi', 'goodmognring', 'gomdoinr', 'goomoring', 'goomdoring', 'godomoring'])
    async def goodmorning(self, ctx):
        responses = [' GOOD MORNING - KANYE ',
                     "It's a beautiful morning!!!!",
                     ' Hi hi hi hi hi hi hiiiii hiii hi hi hi!!!!',
                     'GET OUT OF BED',
                     'You are late for class James!!!!',
                     'perfect day for a ride ay',
                     'dont forget to make your bed \N{WINKING FACE}',
                     'PLEASE shower, you STINK \N{PILE OF POO}',
                     ' \N{TONGUE} Hello ;) \N{TONGUE}',
                     ' \N{EXPRESSIONLESS FACE} stop waking me up',
                     ' \N{BLUE HEART} \N{BLUE HEART} \N{BLUE HEART} \N{BLUE HEART} \N{BLUE HEART} \N{BLUE HEART} \N{BLUE HEART} \N{BLUE HEART} \N{BLUE HEART} \N{BLUE HEART} \N{BLUE HEART} \N{BLUE HEART} \N{BLUE HEART} \N{BLUE HEART} \N{BLUE HEART}'
                     ]
        await ctx.send(random.choice(responses))

    # Random function testing pythong library and the send function with discord api
    @commands.command(aliases =['_kissme', 'mwah'])
    async def kissme(self, ctx):
        responses = [' \N{KISS} ',
                     ' \N{KISSING FACE}',
                     ' \N{KISSING FACE WITH SMILING EYES}',
                     ' \N{TONGUE}',
                     ' \N{EXPRESSIONLESS FACE} '
                     ]
        await ctx.send(random.choice(responses))

    @commands.command()
    async def quicksearch(self, ctx, *, search_request):

        # declarying an array to store the links in
        responses = []
        
        # URL of page I am scraping
        URL = "https://www.google.com/search?q="+search_request+"&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjv44CC_sXwAhUZyjgGHSgdAQ8Q_AUoAXoECAEQAw&cshid=1620885828054361"
        page = requests.get(URL)

        # Running an html parser with BeautifulSoup
        soup = BeautifulSoup(page.content, 'html.parser')
        image_tags = soup.find_all('img', class_='yWs4tf')
        # Storing every "img" tag into an array of responses, parsing what's after "src" (a link to the image from the website)
        for image_tag in image_tags:
            responses.append(image_tag['src'])
        
        # Choosing a random link to display
        link = random.choice(responses)
        embed=discord.Embed(
            title= 'Requested image: ',
                url=link,
                description="Picture of:\n "+search_request.capitalize(),
                color= discord.Color.blue())

        embed.set_image(url = link)
        async with ctx.typing():
            await asyncio.sleep(0.2)
        await ctx.send(embed=embed)
        



    @commands.command()
    async def search(self, ctx, *, search_request):

        # Comments on how this work in the above function
        # This search function takes longer, I think cause depositphotos dumps their entire galaxy into the GET request
        responses = []
        URL = "https://depositphotos.com/stock-photos/"+search_request+".html?filter=all&sorting=best_sales"
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')
        image_tags = soup.find_all('img', class_='file-container__image _file-image lazyload')
        for image_tag in image_tags:
            responses.append(image_tag['data-src'])


        link = (random.choice(responses))
        embed=discord.Embed(
            url=link,
            title="Guess where?",
            color= discord.Color.random())
        embed.set_image(url=link)
        async with ctx.typing():
            await asyncio.sleep(0.2)
        await ctx.send(embed=embed)


    @commands.command(aliases =['_lie', 'liar'])
    async def lie(self, ctx):
        responses = ['  IM NEVER EVER DRINKING AGAIN',
                     '  Eating ice cream and watermelon with a fork is the best way',
                     '  James is such a generous guy',
                     '  49ers are so good!!! \N{WINKING FACE}'
                     ]
        await ctx.send(random.choice(responses))

    @commands.command(aliases =['_oi', 'oi', 'oii', 'oiii', 'oiiii'])
    async def OI(self, ctx):
        responses = [' what did I do this time?',
                     ' you better be using oi in the correct context',
                     ' OIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII',
                     ' Shut up James',
                     ' Oi is an expression used to attract someones attention, especially in a rough or angry way',
                     ' \N{ANGRY FACE} \N{ANGRY FACE} \N{ANGRY FACE}'
                    ]
        await ctx.send(random.choice(responses))

    @commands.command(aliases =['gonight','gondight', 'godnight','goonight','gdnight','night', 'sleepy','sleep','zeroeye', 'zeroey'])
    async def goodnight(self, ctx,):
            intnum= random.randint(0,200)
            if (intnum <50):
                floatnum = (str)(intnum/25)
            elif (intnum > 50 and intnum < 100):
                floatnum = (str)(intnum/50)
            elif (intnum > 100 and intnum < 150):
                floatnum = (str)(intnum/75)
            else:
                floatnum = (str)(intnum/100)
            embed=discord.Embed(
            title='GOODNIGHT GOODNIGHT GOODNIGHT',
                url="https://www.youtube.com/watch?v=rCSCPujLs14",
                description="Sleep Tight",
                color= discord.Color.random())
            embed.set_thumbnail(url="https://www.vhv.rs/dpng/d/453-4534211_sleeping-clipart-zzz-png-zzz-png-transparent-png.png")
            embed.add_field(name="**Zero EYE???**",value=floatnum +' eye, go to sleep!',inline=True)
            async with ctx.typing():
                await asyncio.sleep(1.5)
            await ctx.send(embed=embed)
            await ctx.send('https://www.youtube.com/watch?v=rCSCPujLs14')


def setup(client):
    client.add_cog(Sammy(client))