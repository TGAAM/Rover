# import modules
# For hosting from Heroku/Github I had to include a Requirements.txt file with the following
'''
discord.py==1.3.3
'''

import discord
import os
import random


# live channel whitelist
# rovers-park
whitelistChannelsLive = [705571242312335431]

# test channel whitelist
# bot-testing, bot-testing-2, bot-testing-3, rovers-laboratory
whitelistChannelsTest = [697060204571000903, 698135978270916678, 698135987225886740, 705578025085042729]


# setup a discord client
client = discord.Client()

# initial setup 
@client.event
async def on_ready():
    # notify the log that it's ready
    print('We have logged in as {0.user}'.format(client))


# message posted
# command identifier is %
@client.event
async def on_message(message):

    # don't respond to itself
    if message.author == client.user:
        return

    # live commands
    if (message.channel.id in whitelistChannelsLive or message.channel.id in whitelistChannelsTest):

        # simple answer/reply command
        if message.content.startswith("%beep"):
            await message.channel.send('Boop!')
            return


    # test only commands
    if (message.channel.id in whitelistChannelsTest):
        
        # champion lance theme
        if message.content.startswith("%champion"):
            await message.channel.send("https://www.youtube.com/watch?v=6ICTd__N1OY")

# start the program
# I had to manually add the bot token to Heroku's config variables
client.run(os.environ['ROVER_TOKEN'])
