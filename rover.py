# import modules
# For hosting from Heroku/Github I had to include a Requirements.txt file with the following
'''
discord.py==1.3.3
'''

import discord, os, random, asyncio, traceback, json
from discord.ext import commands, tasks
from discord.ext.commands import CommandNotFound
from discord.ext.commands import CheckFailure
from discord.ext.commands import MissingRequiredArgument
from datetime import datetime, timedelta

# time to send calendar updates in UTC 24h
calendar_update_send_time = '00:00'

# live channel whitelist
# rovers-park, #the-plaza, #the-roost
whitelistChannelsLive = [705571242312335431, 681923559022788654, 696107732260093963]

# test channel whitelist
# rovers-laboratory, #gyroid-gallery
whitelistChannelsTest = [705578025085042729, 681948931491364876]

# dev channel whitelist
# rovers-development
whitelistChannelsDev = [707608424543682670]

# mod roles
# prime, overlord, island staff
modRoles = [689120404664746018, 689120151362469924, 681917732123312188]


# setup a discord client and bot commands
#client = discord.Client()
bot = commands.Bot(command_prefix="%", case_insensitive=True)

# we don't need no stinking helpful help menu
bot.remove_command("help")

# don't work in DMs
@bot.check
async def globally_block_dms(ctx):
    return ctx.guild is not None

# whitelist checks
async def is_live_room(ctx):
    return (ctx.channel.id in whitelistChannelsLive or ctx.channel.id in whitelistChannelsTest or ctx.channel.id in whitelistChannelsDev)

async def is_test_room(ctx):
    return (ctx.channel.id in whitelistChannelsTest or ctx.channel.id in whitelistChannelsDev)

async def is_dev_room(ctx):
    return (ctx.channel.id in whitelistChannelsDev)

async def is_mod(ctx):
    # look through the list of mod roles and check if the user has one
    for roleID in modRoles:
        role = ctx.guild.get_role(roleID)
        if (role in ctx.author.roles):
            # only need one match to be valid
            return True
    
    # nothing found so not a mod
    return False


# initial setup 
@bot.event
async def on_ready():
    # notify the log that it's ready
    print('We have logged in as ' + str(bot.user.name) + ' with ID ' + str(bot.user.id))




"""
Live commmands
"""
@bot.command()
@commands.check(is_live_room)
async def banner(ctx):
    #embed=discord.Embed(description = "Banner contest winner: Angel", color=0xffc572)
    #embed.set_image(url="https://i.imgur.com/3VkhfsO.jpg")
    #await ctx.send(embed=embed)
    await ctx.send("Banner contest winner: Angel\nhttps://i.imgur.com/3VkhfsO.jpg")
    return

@bot.command()
@commands.check(is_live_room)
async def showtime(ctx):
    #embed=discord.Embed(description = "Showtime photo contest winner: Hero", color=0xffc572)
    #embed.set_image(url="https://i.imgur.com/IZwBWSq.png")
    await ctx.send("Showtime photo contest winner: Hero\nhttps://i.imgur.com/IZwBWSq.png")
    #await ctx.send(embed=embed)
    return

@bot.command(aliases = ["zorakas"])
@commands.check(is_live_room)
async def hero(ctx):
    responses = ("https://feen.us/bkyfuam7.gif"
                , "https://feen.us/h2j7k9.gif")
    choice = random.randint(0,len(responses)-1)
    await ctx.send(responses[choice])
    return

@bot.command()
@commands.check(is_live_room)
async def kuma(ctx):
    await ctx.send("https://media.discordapp.net/attachments/539348593711120384/717197247640502272/gulliflourish.gif")
    return

@bot.command()
@commands.check(is_live_room)
async def shay(ctx):
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

@bot.command()
@commands.check(is_live_room)
async def kaylen(ctx):
    responses = ("https://66.media.tumblr.com/10f56e3e98ea49ecfe7a77257033617e/tumblr_pe6ur7YOQJ1vg5ufe_400.gif"
                , "https://data.whicdn.com/images/315087978/original.gif"
                , "https://i.pinimg.com/originals/5c/43/9c/5c439c7f1d7d39474d81b86cc68a7413.gif")
    choice = random.randint(0,len(responses)-1)
    await ctx.send(responses[choice])
    return

@bot.command(aliases = ["bongocat"])
@commands.check(is_live_room)
async def bongo(ctx):
    await ctx.send("https://bongo.cat/")
    return

@bot.command(aliases = ["digging", "gus"])
@commands.check(is_live_room)
async def dig(ctx):
    await ctx.send("https://www.youtube.com/watch?v=YyXs4qfZV_U")
    return

@bot.command(aliases = ["turnips"])
@commands.check(is_live_room)
async def turnip(ctx):
    embed=discord.Embed(description="https://discordapp.com/channels/681917060011655179/686356524385173553/709480670237294682", color=0xffc572)
    await ctx.send(embed=embed)
    return

@bot.command()
@commands.check(is_live_room)
async def myrrien(ctx):
    embed=discord.Embed(description="hullo gentlepeople", color=0xffc572)
    await ctx.send(embed=embed)
    return

@bot.command(aliases = ["ari"])
@commands.check(is_live_room)
async def aro(ctx):
    await ctx.send("<:isauwu:691633580606095400>")
    return

@bot.command(aliases = [".", "davise", "doт", "shower", "dabisc"])
@commands.check(is_live_room)
async def dot(ctx):
    responses = ("WHO PING ME?", "brb shower")
    choice = random.randint(0,len(responses)-1)
    embed=discord.Embed(description=responses[choice], color=0xffc572)
    await ctx.send(embed=embed)
    return

@bot.command(aliases = ["tgaam", "tgam", "tgm"])
@commands.check(is_live_room)
async def tg(ctx):
    embed=discord.Embed(title="<:haunter:689169011866730720> Now calling TGAAM <:haunter:689169011866730720>", description="Please hold.", color=0xffc572)
    embed.add_field(name="...", value="...")
    embed.set_footer(text="Must be doing something %important")
    await ctx.send(embed=embed)
    return

@bot.command()
@commands.check(is_live_room)
async def uncool(ctx):
    embed=discord.Embed(color=0xffc572)
    embed.set_image(url="https://cdn.discordapp.com/attachments/686356524385173553/707577611303256064/7lzcc2z1r2x41.png")
    await ctx.send(embed=embed)
    return

@bot.command()
@commands.check(is_live_room)
async def spring(ctx):
    embed=discord.Embed(description = "Spring photo contest winner: Renna",color=0xffc572)
    embed.set_image(url="https://i.imgur.com/B5v5iFJ.png")
    await ctx.send(embed=embed)
    return

@bot.command()
@commands.check(is_live_room)
async def phan(ctx):
    embed=discord.Embed(description="it me", color=0xffc572)
    embed.set_thumbnail(url="https://i.imgur.com/yOS4rdj.png")
    await ctx.send(embed=embed)
    return

@bot.command()
@commands.check(is_live_room)
async def yeet(ctx):
    await ctx.send("https://clips.twitch.tv/GorgeousOriginalPresidentRedCoat")
    return

@bot.command()
@commands.check(is_live_room)
async def killager(ctx):
    await ctx.send("https://gfycat.com/infantileearlybudgie")
    return

@bot.command()
@commands.check(is_live_room)
async def important(ctx):
    await ctx.send("https://www.youtube.com/watch?v=LVrYnLABnr4")
    return

@bot.command()
@commands.check(is_live_room)
async def kk(ctx):
    songlist = ["https://www.youtube.com/watch?v=O5069uLjZJ0", "https://www.youtube.com/watch?v=cMo_tA4jQzE", "https://www.youtube.com/watch?v=fGccYO16Dr0"
                ,  "https://www.youtube.com/watch?v=eOmbWmhLg8Q", "https://www.youtube.com/watch?v=sy13B7AJwAo", "https://www.youtube.com/watch?v=xDV4pfH74Ig"
                , "https://www.youtube.com/watch?v=79DQ8aeS20M", "https://www.youtube.com/watch?v=2AxndX0apoM&t=5s","https://www.youtube.com/watch?v=2AxndX0apoM"
                , "https://www.youtube.com/watch?v=In0WGlHKsLE", "https://www.youtube.com/watch?v=j77TrwS25q4"
                ]

    songNum = random.randint(0, len(songlist)-1)
    await ctx.send(songlist[songNum])
    return

@bot.command()
@commands.check(is_live_room)
async def savage(ctx):
    embed=discord.Embed(color=0xffc572)
    embed.set_image(url="https://i.imgur.com/By6QI1W.png")
    await ctx.send(embed=embed)
    return


@bot.command()
@commands.check(is_live_room)
async def roll(ctx, die):
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

@bot.command()
@commands.check(is_live_room)
async def flavor(ctx):
    embed=discord.Embed(description="Manila is my favorite flavor of clam", color=0xffc572)
    await ctx.send(embed=embed)
    return

@bot.command(aliases = ["helpme"])
@commands.check(is_live_room)
async def help(ctx):
    embed=discord.Embed(description="I don't need any help right now.\nBut thanks for asking!", color=0xffc572)
    await ctx.send(embed=embed)
    return

@bot.command(aliases = ["hey", "hello", "howdy", "hola"])
@commands.check(is_live_room)
async def hi(ctx):
    embed=discord.Embed(description="Hey there buddy", color=0xffc572)
    await ctx.send(embed=embed)
    return

@bot.command()
@commands.check(is_live_room)
async def ping(ctx):
    embed=discord.Embed(description="Pong!", color=0xffc572)
    await ctx.send(embed=embed)
    return

@bot.command()
@commands.check(is_live_room)
async def beep(ctx):
    embed=discord.Embed(description="Boop!", color=0xffc572)
    await ctx.send(embed=embed)
    return

@bot.command()
@commands.check(is_live_room)
async def join(ctx):
    embed=discord.Embed(description=".john", color=0xffc572)
    await ctx.send(embed=embed)
    return

@bot.command()
@commands.check(is_live_room)
async def john(ctx):
    embed=discord.Embed(description="You are already queued", color=0xffc572)
    await ctx.send(embed=embed)
    return

@bot.command()
@commands.check(is_live_room)
async def rayray(ctx):
    embed=discord.Embed(title="@ everyone I've got Raymond in boxes for whoever wants him.", description="edit: nm, sold for 1000 tickets.", color=0xffc572)
    await ctx.send(embed=embed)
    return

@bot.command()
@commands.check(is_live_room)
async def champion(ctx):
    await ctx.send("https://www.youtube.com/watch?v=6ICTd__N1OY")
    return

@bot.command()
@commands.check(is_live_room)
async def gofish(ctx):
    embed=discord.Embed(description="You caught a sea bass! \n I'd give it a C+!", color=0xffc572)
    await ctx.send(embed=embed)
    return

@bot.command()
@commands.check(is_live_room)
async def gmax(ctx):
    await ctx.send("<:gmax_gengar:696490246057099304>")
    return

@bot.command()
@commands.check(is_live_room)
async def party(ctx):
    embed=discord.Embed(title="🥳 Party Time! 🥳", color=0xffc572)
    await ctx.send(embed=embed)
    return

@bot.command(aliases = ["wooper"])
@commands.check(is_live_room)
async def woop(ctx):
    embed=discord.Embed(title="Woop Woop!", color=0xffc572)
    embed.set_image(url="https://img.pokemondb.net/artwork/wooper.jpg")
    await ctx.send(embed=embed)
    return

@bot.command(aliases = ["appeal", "appealing", "banana"])
@commands.check(is_live_room)
async def peel(ctx):
    await ctx.send("https://www.youtube.com/watch?v=4yHijxLoAPA")
    return

async def timed_jobs():
    await bot.wait_until_ready()
    while not bot.is_closed():
        now = datetime.strftime(datetime.now(), '%H:%M') 

        # calendar events
        if now == calendar_update_send_time:
            #print (now + "-------------------------------")
            guild = bot.get_guild(681917060011655179)
            channel = guild.get_channel(731478991881371690)

            send_date = datetime.strftime(datetime.now(), '%B-%d') 
            await post_events(channel, send_date)
            time = 90
        else:
            #print(now)
            time = 30
        await asyncio.sleep(time)


@bot.command()
@commands.check(is_live_room)
async def today(ctx):
    now = datetime.strftime(datetime.now(), '%B-%d') 
    await post_events(ctx.channel, now)
    return

@bot.command()
@commands.check(is_live_room)
async def tomorrow(ctx):
    now = datetime.strftime(datetime.now() + timedelta(days = 1), '%B-%d') 
    await post_events(ctx.channel, now)
    return

@bot.command()
@commands.check(is_live_room)
async def yesterday(ctx):
    now = datetime.strftime(datetime.now() - timedelta(days = 1), '%B-%d') 
    await post_events(ctx.channel, now)
    return


@bot.command()
@commands.check(is_live_room)
async def date(ctx, now):
    await post_events(ctx.channel, now)
    return

async def post_events(channel, now):
    with open('resources/ac_events.json') as f:
                data = json.load(f)

    date_details = data[now.lower()]
    embed=discord.Embed(title="Event plans for " + now, description=date_details["event"], color=0xffc572)
    await channel.send(embed=embed)
    return


"""
Test only commands
"""
@bot.command()
@commands.check(is_test_room)
async def exampletest(ctx):
    await ctx.send("This is a test only command")
    return

@bot.command()
@commands.check(is_test_room)
async def amIMod(ctx):
    if (await is_mod(ctx)):
        await ctx.send("You are a mod " + str(ctx.author.name))
    else:
        await ctx.send("You are not a mod " + str(ctx.author.name))
    return

"""
Dev only commands
"""
@bot.command()
@commands.check(is_dev_room)
async def exampleDevCommand(ctx):
    await ctx.send("This is a dev only command")
    return


# error handling
@bot.event
async def on_command_error(ctx, error):
    # ignore errors that are invalid commands or calls from failed checks for now
    if isinstance(error, CommandNotFound):
        return
    elif isinstance(error, CheckFailure):
        return
    elif isinstance(error, MissingRequiredArgument):
        await ctx.send("You need to include more details for this command")
        return

    raise error



# start the program
bot.loop.create_task(timed_jobs())
bot.run(os.environ['ROVER_TOKEN'])