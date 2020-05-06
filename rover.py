# import modules
# For hosting from Heroku/Github I had to include a Requirements.txt file with the following
'''
discord.py==1.3.3
'''

import discord
import os
import random
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.ext.commands import CheckFailure
from discord.ext.commands import MissingRequiredArgument


# live channel whitelist
# rovers-park
whitelistChannelsLive = [705571242312335431]

# test channel whitelist
# rovers-laboratory
whitelistChannelsTest = [705578025085042729]

# dev channel whitelist
# rovers-laboratory
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
    print (modRoles)
    print (ctx.author.roles)
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
async def spring(ctx):
    await ctx.send("https://imgur.com/a/MtrT5IZ")
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
    await ctx.send("https://www.youtube.com/watch?v=-4AFLKoGC3M")
    return

@bot.command()
@commands.check(is_live_room)
async def savage(ctx):
    await ctx.send("https://imgur.com/a/sceCpoM")
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
    await ctx.send("You rolled a " +str(roll))
    return

@bot.command()
@commands.check(is_live_room)
async def banner(ctx):
    await ctx.send("https://imgur.com/a/D5UnEZK")
    return

@bot.command()
@commands.check(is_live_room)
async def flavor(ctx):
    await ctx.send("Manila is my favorite flavor of clam!")
    return

@bot.command()
@commands.check(is_live_room)
async def help(ctx):
    await ctx.send("I don't need any help right now.\nBut thanks for asking!")
    return

@bot.command()
@commands.check(is_live_room)
async def hi(ctx):
    await ctx.send("Hey there buddy")
    return

@bot.command()
@commands.check(is_live_room)
async def ping(ctx):
    await ctx.send("Pong!")
    return

@bot.command()
@commands.check(is_live_room)
async def beep(ctx):
    await ctx.send("Boop!")
    return

@bot.command()
@commands.check(is_live_room)
async def join(ctx):
    await ctx.send(".john")
    return

@bot.command()
@commands.check(is_live_room)
async def rayray(ctx):
    await ctx.send("@ everyone I've got Raymond in boxes for whoever wants him.\n\nedit: nm, sold for 1000 tickets.")
    return

@bot.command()
@commands.check(is_live_room)
async def champion(ctx):
    await ctx.send("https://www.youtube.com/watch?v=6ICTd__N1OY")
    return

@bot.command()
@commands.check(is_live_room)
async def gofish(ctx):
    await ctx.send("You caught a sea bass! \n I'd give it a C+!")
    return

@bot.command()
@commands.check(is_live_room)
async def gmax(ctx):
    await ctx.send("<:gmax_gengar:696490246057099304>")
    return

@bot.command()
@commands.check(is_live_room)
async def party(ctx):
    await ctx.send("🥳 Party Time! 🥳")
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
# I had to manually add the bot token to Heroku's config variables
bot.run(os.environ['ROVER_TOKEN'])