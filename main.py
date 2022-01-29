import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')
client.remove_command("help")

token = ""


@client.event
async def on_ready():
    print(f'logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if message.content.startswith('$join'):
        channel = message.author.voice.channel
        await channel.connect()
        message.guild.voice_client.play(discord.FFmpegPCMAudio(source="lead-farm.mp3"))
    else:
        await message.sent("You are not in voice channel")


@client.event
async def on_voice_state_update(member, before, after):
    if member.guild.voice_client:
        if '{0.user}'.format(client) != str(member) and after.channel is not None:
            member.guild.voice_client.play(discord.FFmpegPCMAudio(source="lead-farm.mp3"))


client.run(token)
