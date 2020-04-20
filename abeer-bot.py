import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix='@')

token = ("")


@client.event
async def on_ready():
    print('Bot is ready.')


@client.command()
async def ping(ctx):
    await ctx.send(f"pong!! {round(client.latency *1000 )} ms")
    pass


@client.command(aliases=["qus"])
async def Qus(ctx, *, qus):
    res = ["It is certain.",
           "It is decidedly so.",
           "Without a doubt.",
           "Yes - definitely.",
           "You may rely on it.",
           "As I see it, yes.",
           "Most likely.",
           "Outlook good.",
           "Yes.",
           "Signs point to yes.",
           "Reply hazy, try again.",
           "Ask again later.",
           "Better not tell you now.",
           "Cannot predict now.",
           "Concentrate and ask again.",
           "Don't count on it.",
           "My reply is no.",
           "My sources say no.",
           "Outlook not so good.",
           "Very doubtful."]
    await ctx.send(f"qus: {qus}\nAns: {random.choice(res)}")
    pass


@client.command()
async def on_member_join(self, member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
        await guild.system_channel.send(to_send)


client.run(token)
