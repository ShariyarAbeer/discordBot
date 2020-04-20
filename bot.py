import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix='!')


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


client.run('token)
