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

# live channel whitelist
# rovers-park
whitelistChannelsLive = [705571242312335431]

# test channel whitelist
# bot-testing, bot-testing-2, bot-testing-3, rovers-laboratory
whitelistChannelsTest = [697060204571000903, 698135978270916678, 698135987225886740, 705578025085042729]


# setup a discord client and bot commands
#client = discord.Client()
bot = commands.Bot(command_prefix="%", case_insensitive=True)

# don't work in DMs
@bot.check
async def globally_block_dms(ctx):
    return ctx.guild is not None

# whitelist check
async def is_live_room(ctx):
    return (ctx.channel.id in whitelistChannelsLive or ctx.channel.id in whitelistChannelsTest)

async def is_test_room(ctx):
    return (ctx.channel.id in whitelistChannelsTest)

# initial setup 
@bot.event
async def on_ready():
    # notify the log that it's ready
    print('We have logged in as ' + str(bot.user.name) + ' with ID ' + str(bot.user.id))




"""
# initial setup 
@client.event
async def on_ready():
    # notify the log that it's ready
    print('We have logged in as {0.user}'.format(client))
"""

"""
Live commmands
"""

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
async def champion(ctx):
    await ctx.send("https://www.youtube.com/watch?v=6ICTd__N1OY")
    return

@bot.command()
@commands.check(is_live_room)
async def fishing(ctx):
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



# error handling
@bot.event
async def on_command_error(ctx, error):
    # ignore errors that are invalid commands or calls from failed checks for now
    if isinstance(error, CommandNotFound):
        return
    elif isinstance(error, CheckFailure):
        return

    raise error



# start the program
# I had to manually add the bot token to Heroku's config variables
bot.run(os.environ['ROVER_TOKEN'])