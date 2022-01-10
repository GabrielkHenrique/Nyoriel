from discord.ext import commands
from decouple import config
import discord



bot = commands.Bot("!")


bot.load_extension('manager')
bot.load_extension('commands.cripto')
bot.load_extension('commands.image')
bot.load_extension('commands.reactions')
bot.load_extension('commands.smart')
bot.load_extension('commands.talk')
bot.load_extension('tasks.dates')

TOKEN = config("TOKEN")
bot.run(TOKEN)

