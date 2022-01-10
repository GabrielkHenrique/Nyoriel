import requests
from discord.ext import commands

class Cripto(commands.Cog):
    """Crypto"""
    def __init__(self, bot):
        self.bot = bot
    @commands.command( help="Verifica o preço de um par na Binance")
    async def binance(self,ctx, coin, base):
        try:
            response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}")
            #BNB BTC 

            data = response.json()
            price = data.get("price")
            if price:
                await ctx.send(f"O valor do par {coin}/{base} é {price}")
            else:
                await ctx.send(f"O valor do par {coin}/{base} é invalido")
        except Exception as error: 
            await ctx.send("Ops alguma coisa deu errada! tente novamente mais tarde")
            print(error)

def setup(bot):
    bot.add_cog(Cripto(bot))

