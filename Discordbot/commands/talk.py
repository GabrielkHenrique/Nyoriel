from discord.ext import commands
import discord
import requests

class Talks(commands.Cog):
    """Talk with user"""
    def __init__(self, bot):
        self.bot = bot
    @commands.command( name = "oi" , help="Envia um Oi!")
    async def send_hello(self,ctx):
        name = ctx.author.name
        response = "Olá, " + name

        await ctx.send(response)
    @commands.command( name = "segredo", help="Te envia um segredo no privado" )
    async def secret(self,ctx):
        try:
            await ctx.author.send("Secreto")
        except discord.errors.Forbidden:
            await ctx.send("Não posso te enviar um segredo! Habilite receber mensagens de qualquer pessoa no servido(opções -> privacidade)")
    @commands.command(name = "conselho",  help="Te da um conselho mas esse comando só está disponivel em inglês")
    async def conselho(self,ctx):
        response = requests.get('https://api.adviceslip.com/advice')
    
        data = response.json()
        advice = data.get("slip")
        vai = advice.get("advice")
        await ctx.send(vai)
    @commands.command( name = "comandos",  help="Mostra alguns comandos" )
    async def comandos(self,ctx):
        responde = "Ainda estou na versão alpha por isso meus comandos mudam constantemente! sinto muito mas não tenho nenhuma lista para te dar agora"
        await ctx.send(responde)
    


def setup(bot):
    bot.add_cog(Talks(bot))

