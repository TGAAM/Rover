import discord, traceback
from discord.ext import commands
import checks_list


def setup(bot):
        bot.add_cog(Mods(bot))


class Mods (commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

 
    @commands.command(aliases = ["talk"], hidden = True)
    @commands.check(checks_list.is_mod)
    async def speak(self, ctx, channelID, *, message):
        try:
            channel = self.bot.get_channel(int(channelID))

            try:
                await channel.send(message)

            except:
                await ctx.send ("Hmm, had trouble sending that message")
                traceback.print_exc()

        except:
                await ctx.send ("I can't find that channel")

        return

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if len(before.roles) < len(after.roles):
            # The user has gained a new role, so lets find out which one
            newRole = next(role for role in after.roles if role not in before.roles)

            if (newRole.id in checks_list.alertRoles):
                for channelID in checks_list.whitelistChannelsRover:
                    try: 
                        channel = self.bot.get_channel(channelID)
                        if (channel.guild == after.guild):
                            pingRole = checks_list.primaryRoles[channel.guild.id]
                            msg = "<@&" + str(pingRole) + "> user <@" + str(after.id) + "> has been given the *" + str(newRole) + "* role"
                            await channel.send(msg)

                    except:
                        traceback.print_exc()