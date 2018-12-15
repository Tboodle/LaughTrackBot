from discord.ext.commands import Bot
from discord import voice_client
from discord.ext import commands
import discord
import asyncio
import time

CLIENT_ID =  	305046221977026570
CLIENT_SECRET = "hc3FoSAT3Mp8_zryHNd9BF2YEmSSJfoT"
TOKEN = 	"MzA1MDQ2MjIxOTc3MDI2NTcw.C9vs3g.F_lj7AsU8h0-9wrp22iXzs9VCgc"

class Audio:

    def __init__(self, bot):
        self.bot = bot
        self.quotes = {}
        self.client = discord.Client()
        self.client.start(TOKEN);

    @commands.command(pass_context=True, no_pm=True)
    async def haha(self, ctx):

        #try:
        voice = await self.bot.join_voice_channel(ctx.message.author.voice.voice_channel)
        playerHaha = voice.create_ffmpeg_player("clips/" + "haha.wav")
        #except:
        #    print("Could not join voice channel")
    
        await self.bot.delete_message(ctx.message)
        playerHaha.start()
        time.sleep(4)
        playerHaha.stop()
        await voice.disconnect()


    @commands.command(pass_context=True, no_pm=True)
    async def run(self, ctx):

        try:
            voice = await self.bot.join_voice_channel(ctx.message.author.voice_channel)
            playerRun = voice.create_ffmpeg_player("clips/" + "run.wav")
        except:
            print("Could not join voice channel")

        await self.bot.delete_message(ctx.message)
        playerRun.start()
        time.sleep(4)
        playerRun.stop()
        await voice.disconnect()

    @commands.command(pass_context=True, no_pm=True)
    async def down(self, ctx):

        try:
            voice = await self.bot.join_voice_channel(ctx.message.author.voice_channel)
            player = voice.create_ffmpeg_player("clips/" + "downWithTheSickness.wav")
        except:
            print("Could not join voice channel")
    
        await self.bot.delete_message(ctx.message)
        player.start()
        time.sleep(4)
        player.stop()
        await voice.disconnect()


#    @commands.command(pass_context=True, no_pm=True)
#    async def yes(self, ctx):

#        try:
#            voice = await self.bot.join_voice_channel(ctx.message.author.voice_channel)
#        except:
#            print("Could not join voice channel")
    
#        await self.bot.delete_message(ctx.message)
#        player = voice.create_ffmpeg_player("clips/" + "yes.wav")
#        player.start()
#        time.sleep(4)
#        player.stop()
#        await voice.disconnect()

def main():
    bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), description='Haha bot')
    bot.add_cog(Audio(bot))
    bot.run(TOKEN)
    
if __name__ == "__main__":
    main()
