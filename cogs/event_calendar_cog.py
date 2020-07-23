import discord, asyncio, traceback, json
from discord.ext import commands, tasks
import checks_list
from datetime import datetime, timedelta

# time to send calendar updates in UTC 24h
calendar_update_send_time = '00:00'

def setup(bot):
        bot.add_cog(Event_Calendar(bot))
        

class Event_Calendar (commands.Cog):
    def __init__ (self, bot):
        self.bot = bot
        self.bot.loop.create_task(self.timed_jobs())


    async def timed_jobs(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            now = datetime.strftime(datetime.now(), '%H:%M') 

            # calendar events
            if now == calendar_update_send_time:
                #print (now + "-------------------------------")
                guild = self.bot.get_guild(681917060011655179)
                channel = guild.get_channel(731478991881371690)

                send_date = datetime.strftime(datetime.now(), '%B-%d') 
                await self.post_events(channel, send_date)
                time = 90
            else:
                #print(now)
                time = 30
            await asyncio.sleep(time)


    @commands.command()
    @commands.check(checks_list.is_live_room)
    async def today(self, ctx):
        now = datetime.strftime(datetime.now(), '%B-%d') 
        await self.post_events(ctx.channel, now)
        return

    @commands.command()
    @commands.check(checks_list.is_live_room)
    async def tomorrow(self, ctx):
        now = datetime.strftime(datetime.now() + timedelta(days = 1), '%B-%d') 
        await self.post_events(ctx.channel, now)
        return

    @commands.command()
    @commands.check(checks_list.is_live_room)
    async def yesterday(self, ctx):
        now = datetime.strftime(datetime.now() - timedelta(days = 1), '%B-%d') 
        await self.post_events(ctx.channel, now)
        return


    @commands.command()
    @commands.check(checks_list.is_live_room)
    async def date(self, ctx, date):
        await self.post_events(ctx.channel, date)
        return

    async def post_events(self, channel, date):
        with open('resources/ac_events.json') as f:
                data = json.load(f)

        date_details = data[date.lower()]
        embed=discord.Embed(title="Event plans for " + date, description=date_details["event"], color=0xffc572)
        await channel.send(embed=embed)
        return