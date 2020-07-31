import discord, traceback
from discord.ext import commands
import checks_list



def setup(bot):
        bot.add_cog(Mailbox(bot))


class Mailbox (commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.command(pass_context=True, brief="DM User", help="*dm {userID} {message}")
    @commands.check(checks_list.is_rover_room)
    async def dm(self, ctx, userID, *, message):

        user = ctx.guild.get_member(int(userID))
        if (user is None):
            await ctx.send("User not found in this server")
        else:
            try:
                await user.send(message)
            except:
                await ctx.send ("Unable to send that message")
                traceback.print_exc()


        embed = discord.Embed(title="📨 Rover DM Sent 📨", color=0xffc572)
        embed.add_field(name = "Sender", value = ctx.author.mention)
        embed.add_field(name = "Recepient", value = user.mention)
        embed.add_field(name = "Message", value = message)
        await ctx.send (embed = embed)

        await ctx.message.delete()
        return


    @commands.Cog.listener()
    async def on_message(self, message):

        if message.guild is None and message.author != self.bot.user:
            for channelID in checks_list.whitelistChannelsRover:
                try:                    
                    channel = self.bot.get_channel(channelID)
                    fileList = []
                    fileNames = []
                    for attach in message.attachments:
                        singleFile = await attach.to_file()
                        fileList.append(singleFile)
                        fileNames.append (singleFile.filename)

                    embed = discord.Embed(title="📩 Rover DM Received 📩", color=0xffc572)
                    embed.add_field(name = "Sender", value = message.author.mention)

                    if (message.content != ""):
                        embed.add_field(name = "Message", value = message.content)
                    
                    if (len(fileNames) > 0):
                        embed.add_field(name = "Attachments", value = str(fileNames))
                    
                    await channel.send (embed = embed, files=fileList)
                except:
                        traceback.print_exc()

        return

