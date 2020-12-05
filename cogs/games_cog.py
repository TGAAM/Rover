import discord, random
from discord.ext import commands
import checks_list


def setup(bot):
        bot.add_cog(Games(bot))


class Games (commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.command()
    @commands.check(checks_list.is_live_room)
    async def kk(self, ctx):
        songlist = ["https://www.youtube.com/watch?v=O5069uLjZJ0", "https://www.youtube.com/watch?v=cMo_tA4jQzE"
                    ,  "https://www.youtube.com/watch?v=eOmbWmhLg8Q", "https://www.youtube.com/watch?v=sy13B7AJwAo", "https://www.youtube.com/watch?v=xDV4pfH74Ig"
                    , "https://www.youtube.com/watch?v=79DQ8aeS20M", "https://www.youtube.com/watch?v=2AxndX0apoM&t=5s","https://www.youtube.com/watch?v=2AxndX0apoM"
                    , "https://www.youtube.com/watch?v=In0WGlHKsLE", "https://www.youtube.com/watch?v=j77TrwS25q4"
                    ]

        songNum = random.randint(0, len(songlist)-1)
        await ctx.send(songlist[songNum])
        return


    @commands.command(brief="roll X", help="Ex: %roll 5")
    @commands.check(checks_list.is_live_room)
    async def roll(self, ctx, die):
        try:
            assert int(die) == float(die)
            die = int(die)
            assert die >= 1
            
        except:
            await ctx.send("You can't roll a die with " + str(die) + " sides, smh")
            return
        roll = random.randint(1, die)
        result = "You rolled a " + str(roll)
        embed=discord.Embed(description=result, color=0xffc572)
        await ctx.send(embed=embed)
        return


    @commands.command()
    @commands.check(checks_list.is_live_room)
    async def ping(self, ctx):
        embed=discord.Embed(description="Pong!", color=0xffc572)
        await ctx.send(embed=embed)
        return

    @commands.command()
    @commands.check(checks_list.is_live_room)
    async def beep(self, ctx):
        embed=discord.Embed(description="Boop!", color=0xffc572)
        await ctx.send(embed=embed)
        return


    @commands.command()
    @commands.check(checks_list.is_live_room)
    async def gofish(self, ctx):
        embed=discord.Embed(description="You caught a sea bass! \n I'd give it a C+!", color=0xffc572)
        await ctx.send(embed=embed)
        return

