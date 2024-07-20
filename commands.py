import discord
from discord.ext import commands
from discord.commands import slash_command

r = open('guild_ids.txt', 'r', encoding='UTF-8') #open guild_ids file
data = r.read() #read guild_ids file
r.close() #close guild_ids file

guild_ids = [data] # guild_ids

class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=guild_ids)
    async def hi(self,ctx: discord.ApplicationContext):
        await ctx.respond('hi!')
    @slash_command()
    async def ping(self,ctx: discord.ApplicationContext):
        await ctx.respond('pong')
    @slash_command()
    async def hello(self,ctx: discord.ApplicationContext):
        await ctx.respond('hello')

def setup(bot): #add commands
    bot.add_cog(Example(bot))