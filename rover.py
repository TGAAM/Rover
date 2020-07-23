# import modules
'''
discord.py==1.3.4
'''

import discord, os, random, asyncio, traceback
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.ext.commands import CheckFailure
from discord.ext.commands import MissingRequiredArgument
import checks_list

# cogs
cogsList = ['cogs.event_calendar_cog', 'cogs.games_cog', 'cogs.memes_cog'
            , 'cogs.mods_cog', 'cogs.vanity_cog', 'cogs.mailbox_cog'
            ]



# setup a discord client and bot commands
#client = discord.Client()
bot = commands.Bot(command_prefix="%", case_insensitive=True)
#bot = commands.Bot(command_prefix="^", case_insensitive=True)



# no commands from DMs
@bot.check
async def globally_block_dms(ctx):
    return ctx.guild is not None


# initial setup 
@bot.event
async def on_ready():
    cogs = cogsList
    for cog in cogs:
        try:
            bot.load_extension(cog)
        except Exception as e:
            print("Problem with loading: " + str(cog))
            traceback.print_exc()


    # notify the log that it's ready
    print('We have logged in as ' + str(bot.user.name) + ' with ID ' + str(bot.user.id))




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
bot.run(os.environ['ROVER_TOKEN'])