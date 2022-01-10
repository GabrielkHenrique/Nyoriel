from discord.ext import commands
import discord

class Image(commands.Cog):
    """Send Image"""
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="foto", help="Te envia uma foto aleatoria" )
    async def get_random_image(self,ctx):
        url_image = "https://picsum.photos/300/300"
        embed = discord.Embed(
            title = "Resultado da busca",
            description = "PS: a busca é totalmente aleatoria",
            color = 0xFFCB77
        )

        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed.set_image(url=url_image)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Image(bot))

