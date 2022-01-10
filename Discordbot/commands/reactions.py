from discord.ext import commands

class Reaction(commands.Cog):
    """Reaction with user"""
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_reaction_add(self,reaction, user):
        print(reaction.emoji)
        if reaction.emoji == "👍":
            role = user.guild.get_role(925497538402983966)
            await user.add_roles(role)
        elif  reaction.emoji == "👎" :
            role = user.guild.get_role(925497586490703933)
            await user.add_roles(role)





def setup(bot):
    bot.add_cog(Reaction(bot))

