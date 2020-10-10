import discord, random
from discord.ext import commands
import checks_list


def setup(bot):
        bot.add_cog(People(bot))


class People (commands.Cog):
    def __init__ (self, bot):
        self.bot = bot


    @commands.command(aliases = ["zorakas"])
    @commands.check(checks_list.is_live_room)
    async def hero(self, ctx):
        responses = ("https://feen.us/bkyfuam7.gif"
                    , "https://feen.us/h2j7k9.gif")
        choice = random.randint(0,len(responses)-1)
        await ctx.send(responses[choice])
        return


    @commands.command()
    @commands.check(checks_list.is_live_room)
    async def kuma(self, ctx):
        await ctx.send("https://media.discordapp.net/attachments/539348593711120384/717197247640502272/gulliflourish.gif")
        return

    @commands.command(aliases = ["daydream", "dream", "dreaming"])
    @commands.check(checks_list.is_live_room)
    async def daydreaming(self, ctx):
        await ctx.send("https://64.media.tumblr.com/7f60ade2a20178b0c3997fcfd5af5381/tumblr_pmtfu3Jib41wsfn4ho1_400.gif")
        return

    @commands.command(hidden = True)
    @commands.check(checks_list.is_live_room)
    async def shay(self, ctx):
        # define the possible responses
        responseList = ["Wait, what?"
                    , "<:rusrs:683806905529008148>"
                    , "A dancing Wooper has appeared. \nhttps://youtu.be/P573r7j5ou4%E2%80%9D"
                    , "Try again later.\nRover is done with your antics."
                    , "FT: Raymond\nLF: 20 Million NMT, 50 trillion bells, and either of your eyeballs (Left is preferred)"
                    , "https://pbs.twimg.com/media/EaCJKhzXsAYxHpq?format=jpg&name=small"
                    ]
        # define the probability of each choice relative to each other
        weightList = [.5, .2, .1, .1, .05, .05]

        # pick a choice
        choice = random.choices(responseList, weights=weightList, k=1)[0]

        # create an embed with the choice. Optional and color can be changed
        #embed=discord.Embed(description=choice, color=0xffc572)

        # send the response
        #await ctx.send(embed=embed)
        await ctx.send(choice)

        # end the command
        return


    @commands.command()
    @commands.check(checks_list.is_live_room)
    async def hanna(self, ctx):
        responses = ("https://media1.giphy.com/media/jqSVaKOtBjFZf1s4Ih/giphy.gif?cid=4d1e4f297b58472da1d318b4af5f034521faf22b6278621d&rid=giphy.gif"
                    , "https://media0.giphy.com/media/Zdm1OZZu1s11AzIHHA/giphy.gif?cid=4d1e4f297b58472da1d318b4af5f034521faf22b6278621d&rid=giphy.gif"
                    , "https://media3.giphy.com/media/QxqlC7oJq7lMJIgQEx/giphy.gif?cid=4d1e4f297b58472da1d318b4af5f034521faf22b6278621d&rid=giphy.gif"
                    , "https://media3.giphy.com/media/U4pL3tfs2xeb2vMJDV/giphy.gif?cid=4d1e4f297b58472da1d318b4af5f034521faf22b6278621d&rid=giphy.gif"
                    )
        choice = random.randint(0,len(responses)-1)
        await ctx.send(responses[choice])
        return

    @commands.command()
    @commands.check(checks_list.is_live_room)
    async def vacation(self, ctx):
        await ctx.send("Vacation Album Contest winner: Hanna\nhttps://i.imgur.com/tAWOWF1.png")
        return

    @commands.command()
    @commands.check(checks_list.is_live_room)
    async def myrrien(self, ctx):
        embed=discord.Embed(description="hullo gentlepeople", color=0xffc572)
        await ctx.send(embed=embed)
        return

    @commands.command()
    @commands.check(checks_list.is_live_room)
    async def frog(self, ctx):
        await ctx.send("https://i.imgur.com/AvakCrW.png")
        return


    @commands.command(aliases = ["ari"])
    @commands.check(checks_list.is_live_room)
    async def aro(self, ctx):
        await ctx.send("<:isauwu:691633580606095400>")
        return

    @commands.command(aliases = [".", "davise", "doт", "shower", "dabisc"])
    @commands.check(checks_list.is_live_room)
    async def dot(self, ctx):
        responses = ("WHO PING ME?", "brb shower")
        choice = random.randint(0,len(responses)-1)
        embed=discord.Embed(description=responses[choice], color=0xffc572)
        await ctx.send(embed=embed)
        return

    @commands.command(aliases = ["tgaam", "tgam", "tgm"])
    @commands.check(checks_list.is_live_room)
    async def tg(self, ctx):
        embed=discord.Embed(title="<:haunter:689169011866730720> Now calling TGAAM <:haunter:689169011866730720>", description="Please hold.", color=0xffc572)
        embed.add_field(name="...", value="...")
        embed.set_footer(text="Must be doing something %important")
        await ctx.send(embed=embed)
        return



    @commands.command()
    @commands.check(checks_list.is_live_room)
    async def phan(self, ctx):
        embed=discord.Embed(description="it me", color=0xffc572)
        embed.set_thumbnail(url="https://i.imgur.com/yOS4rdj.png")
        await ctx.send(embed=embed)
        return



    @commands.command()
    @commands.check(checks_list.is_live_room)
    async def banner(self, ctx):
        #embed=discord.Embed(description = "Banner contest winner: Angel", color=0xffc572)
        #embed.set_image(url="https://i.imgur.com/3VkhfsO.jpg")
        #await ctx.send(embed=embed)
        await ctx.send("Banner contest winner: Angel\nhttps://i.imgur.com/3VkhfsO.jpg")
        return

    @commands.command()
    @commands.check(checks_list.is_live_room)
    async def showtime(self, ctx):
        #embed=discord.Embed(description = "Showtime photo contest winner: Hero", color=0xffc572)
        #embed.set_image(url="https://i.imgur.com/IZwBWSq.png")
        await ctx.send("Showtime photo contest winner: Hero\nhttps://i.imgur.com/IZwBWSq.png")
        #await ctx.send(embed=embed)
        return


    @commands.command()
    @commands.check(checks_list.is_live_room)
    async def kaylen(self, ctx):
        responses = ("https://66.media.tumblr.com/10f56e3e98ea49ecfe7a77257033617e/tumblr_pe6ur7YOQJ1vg5ufe_400.gif"
                    , "https://data.whicdn.com/images/315087978/original.gif"
                    , "https://i.pinimg.com/originals/5c/43/9c/5c439c7f1d7d39474d81b86cc68a7413.gif")
        choice = random.randint(0,len(responses)-1)
        await ctx.send(responses[choice])
        return