import discord
from discord.ext import commands
import datetime

class Smart(commands.Cog):
    """Smart with user"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "calcular" , help="calcula 2 ou uma expressão de numeros")
    async def calculate_expression(self,ctx , expression):   
        expression = "".join(expression)
        responde = eval(expression)
        await ctx.send("A resposta é: " + str(responde))
    #######################################
    @commands.command( name = "hora",  help="Te informa que horas são" )
    async def send_time(self,ctx):
        now = datetime.datetime.now()
        now = now.strftime("%H:%M:%S")
        await ctx.send("Tick e tack agora são " + now)
    #######################################
    @commands.command( name = "clean" )
    async def clear(self,ctx, amount=5):
        await ctx.channel.purge(limit=amount)
    #######################################
    
        



def setup(bot):
    bot.add_cog(Smart(bot))

