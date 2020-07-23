import discord

# live channel whitelist
# rovers-park, #the-plaza, #the-roost
whitelistChannelsLive = [705571242312335431, 681923559022788654, 696107732260093963]

# test channel whitelist
# rovers-laboratory, #gyroid-gallery, #rovers-playroom
whitelistChannelsTest = [705578025085042729, 681948931491364876, 735993247540969513]

# dev channel whitelist
# rovers-development
whitelistChannelsDev = [707608424543682670]

# Rover specific channels whitelist
# rovers-mailbox, rovers=playroom
whitelistChannelsRover = [735521764360060968, 735993247540969513]

# mod roles
# prime, island staff
modRoles = [689120404664746018, 681917732123312188]

# roles to notify team when added
# important-role, 
alertRoles = [735592881972052120]

# primary role for each guild
# Bot Party = Prime, AC = Island Staff
primaryRoles = {689079080892760125:689120404664746018, 681917060011655179:681917732123312188}

# whitelist checks
async def is_live_room(ctx):
    return (ctx.channel.id in whitelistChannelsLive or ctx.channel.id in whitelistChannelsTest or ctx.channel.id in whitelistChannelsDev)

async def is_test_room(ctx):
    return (ctx.channel.id in whitelistChannelsTest or ctx.channel.id in whitelistChannelsDev)

async def is_dev_room(ctx):
    return (ctx.channel.id in whitelistChannelsDev)

async def is_rover_room(ctx):
    return (ctx.channel.id in whitelistChannelsRover)

async def is_mod(ctx):
    # look through the list of mod roles and check if the user has one
    for roleID in modRoles:
        role = ctx.guild.get_role(roleID)
        if (role in ctx.author.roles):
            # only need one match to be valid
            return True
    
    # nothing found so not a mod
    return False
