import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix='')

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


@client.command()
async def rule(ctx):
    await ctx.send("Welcome To Masters of Ravens @everyone\n"
                   " █ Rules █ \n"
                   "1) Use the correct channels.\n"
                   "2) Heart Respect each other and help each other out with questions.\n"
                   "3) Call_me Make sure discussion is related to the channel you’re in.\n"
                   "4) Don’t be nasty, no toxicity.\n"
                   "5) Loudspeaker No advertising your severs into our server.\n"
                   "6) Calling No spamming.\n"
                   "7) Don’t be afraid to ask any questions.\n"
                   "8) Heart Be happy!.\n"

                   "Server link : https://discord.gg/W9dvHUv\n")
    pass


@client.command()
async def role(ctx):
    await ctx.send("role")
    pass


async def on_message(self, message):
    # we do not want the bot to reply to itself
    if message.author.id == self.user.id:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello {0.author.mention}'.format(message))


@client.command()
async def hi(ctx):
    await ctx.send("role")
    pass


client.run(token)
