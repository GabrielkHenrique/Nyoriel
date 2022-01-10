from discord import activity
from discord.ext import commands
from discord.embeds import Embed 
from discord.ext import commands, tasks
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound
from decouple import config
import discord

class Manager(commands.Cog):
    """manage the bot"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        activity = discord.Game(name='Ainda em desonlvimento', type=3)
        await self.bot.change_presence(status=discord.Status.idle, activity=activity)
        print(f"Estou pronto! {self.bot.user}")
        print(f'Ping: {round(self.bot.latency * 1000)}')
        #current_time.start()

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author == self.bot.user:
            return
        if "palavrão" in message.content:
            await message.channel.send(f"Por favor, {message.author.name}, não ofenda os outros!")

            await message.delete()
        

    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Está faltando argumnetos no comando")
        elif isinstance(error, CommandNotFound):
            await ctx.send("Esse comando não está no nosso cardapio")
        else:
            raise error

def setup(bot):
    bot.add_cog(Manager(bot))

