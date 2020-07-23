import discord
from discord.ext import commands
import checks_list


def setup(bot):
        bot.add_cog(Memes(bot))


class Memes (commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    
    @commands.command(aliases = ["bongocat"])
    @commands.check(checks_list.is_live_room)
    async def bongo(self, ctx):
        await ctx.send("https://bongo.cat/")
        return

    @commands.command(aliases = ["digging", "gus"])
    @commands.check(checks_list.is_live_room)
    async def dig(self, ctx):
        await ctx.send("https://www.youtube.com/watch?v=YyXs4qfZV_U")
        return

    @commands.command(aliases = ["turnips"])
    @commands.check(checks_list.is_live_room)
    async def turnip(self, ctx):
        embed=discord.Embed(description="https://discordapp.com/channels/681917060011655179/686356524385173553/709480670237294682", color=0xffc572)
        await ctx.send(embed=embed)
        return



    @commands.command()
    @commands.check(checks_list.is_live_room)
    async def uncool(self, ctx):
        embed=discord.Embed(color=0xffc572)
        embed.set_image(url="https://cdn.discordapp.com/attachments/686356524385173553/707577611303256064/7lzcc2z1r2x41.png")
        await ctx.send(embed=embed)
        return

    @commands.command()
    @commands.check(checks_list.is_live_room)
    async def spring(self, ctx):
        embed=discord.Embed(description = "Spring photo contest winner: Renna",color=0xffc572)
        embed.set_image(url="https://i.imgur.com/B5v5iFJ.png")
        await ctx.send(embed=embed)
        return


    @commands.command()
    @commands.check(checks_list.is_live_room)
    async def yeet(self, ctx):
        await ctx.send("https://clips.twitch.tv/GorgeousOriginalPresidentRedCoat")
        return

    @commands.command()
    @commands.check(checks_list.is_live_room)
    async def killager(self, ctx):
        await ctx.send("https://gfycat.com/infantileearlybudgie")
        return

    @commands.command()
    @commands.check(checks_list.is_live_room)
    async def important(self, ctx):
        await ctx.send("https://www.youtube.com/watch?v=LVrYnLABnr4")
        return


    @commands.command()
    @commands.check(checks_list.is_live_room)
    async def savage(self, ctx):
        embed=discord.Embed(color=0xffc572)
        embed.set_image(url="https://i.imgur.com/By6QI1W.png")
        await ctx.send(embed=embed)
        return


    @commands.command()
    @commands.check(checks_list.is_live_room)
    async def flavor(self, ctx):
        embed=discord.Embed(description="Manila is my favorite flavor of clam", color=0xffc572)
        await ctx.send(embed=embed)
        return
    '''
    @commands.command(aliases = ["helpme"])
    @commands.check(checks_list.is_live_room)
    async def help(self, ctx):
        embed=discord.Embed(description="I don't need any help right now.\nBut thanks for asking!", color=0xffc572)
        await ctx.send(embed=embed)
        return
    '''

    @commands.command(aliases = ["hey", "hello", "howdy", "hola"])
    @commands.check(checks_list.is_live_room)
    async def hi(self, ctx):
        embed=discord.Embed(description="Hey there buddy", color=0xffc572)
        await ctx.send(embed=embed)
        return

    @commands.command()
    @commands.check(checks_list.is_live_room)
    async def join(self, ctx):
        embed=discord.Embed(description=".john", color=0xffc572)
        await ctx.send(embed=embed)
        return

    @commands.command()
    @commands.check(checks_list.is_live_room)
    async def john(self, ctx):
        embed=discord.Embed(description="You are already queued", color=0xffc572)
        await ctx.send(embed=embed)
        return

    @commands.command()
    @commands.check(checks_list.is_live_room)
    async def rayray(self, ctx):
        embed=discord.Embed(title="@ everyone I've got Raymond in boxes for whoever wants him.", description="edit: nm, sold for 1000 tickets.", color=0xffc572)
        await ctx.send(embed=embed)
        return

    @commands.command()
    @commands.check(checks_list.is_live_room)
    async def champion(self, ctx):
        await ctx.send("https://www.youtube.com/watch?v=6ICTd__N1OY")
        return

    @commands.command()
    @commands.check(checks_list.is_live_room)
    async def gmax(self, ctx):
        await ctx.send("<:gmax_gengar:696490246057099304>")
        return

    @commands.command()
    @commands.check(checks_list.is_live_room)
    async def party(self, ctx):
        embed=discord.Embed(title="🥳 Party Time! 🥳", color=0xffc572)
        await ctx.send(embed=embed)
        return

    @commands.command(aliases = ["wooper"])
    @commands.check(checks_list.is_live_room)
    async def woop(self, ctx):
        embed=discord.Embed(title="Woop Woop!", color=0xffc572)
        embed.set_image(url="https://img.pokemondb.net/artwork/wooper.jpg")
        await ctx.send(embed=embed)
        return

    @commands.command(aliases = ["appeal", "appealing", "banana"])
    @commands.check(checks_list.is_live_room)
    async def peel(self, ctx):
        await ctx.send("https://www.youtube.com/watch?v=4yHijxLoAPA")
        return
