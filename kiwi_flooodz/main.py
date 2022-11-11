import datetime
import json
import time
from typing import Literal

import discord
from discord import ButtonStyle, Interaction, app_commands, ui
from discord.app_commands import tree
from discord.ext import commands

import dataProcessor

# Global Variables
embedColor = 0x86f151
serverID = 1038821985288998953
formNum = 0
feedbackChannel = 1038823192363552869
logo = discord.File("LogoNoBG.jpg", filename="LogoNoBG.jpg")
# Get configuration.json
with open("Data\configuration.json", "r") as config:
    data = json.load(config)
    token = data["token"]
    prefix = data["prefix"]

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild = discord.Object(id=serverID))
            self.synced = True
        print(f"logged as {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)

# Load cogs
initial_extensions = [
    "Cogs.help",
    "Cogs.ping"
]

print(initial_extensions)

# Debug Command
@tree.command(guild=discord.Object(id=serverID), name="debug", description="Debug bot")
async def debug(Interaction: discord.Interaction):
    await Interaction.response.send_message(f"bot pinged: {round(client.latency, 2)} ms", ephemeral=True)

# Help Command
@tree.command(guild=discord.Object(id=serverID), name='help', description="Kiwi's Mailbox Service help command")
async def help(Interaction: discord.Interaction):
    helpEmbed = discord.Embed(title='Kiwi Mailbox Service', description='Help Page\n\n**Commands**', color=embedColor)
    helpEmbed.add_field(name='/help', value='Brings you to this page', inline=False)
    helpEmbed.add_field(name='/stats', value='See bot stats', inline=False)
    helpEmbed.add_field(name='/flood ON', value='Start flooding a specific form', inline=False)
    helpEmbed.add_field(name='/flood OFF', value='[Not Implemented]: Stop flooding a specific form', inline=False)
    helpEmbed.add_field(name='/debug', value='Check if bot is online', inline=False)
    
    
    helpEmbed.set_thumbnail(url="attachment://LogoNoBG.jpg")
    await Interaction.response.send_message(file=logo,embed=helpEmbed)

# Statistic Command
@tree.command(guild=discord.Object(id=serverID), name='stats', description='Kiwi Mailbox Service Stats')
async def stats(Interaction: discord.Interaction):
    statsEmbed = discord.Embed(title='Kiwi Mailbox Service Statistics', color=embedColor)
    statsEmbed.add_field(name='Number of forms filled:', value=f'[Aprox]: {dataProcessor.x}')
    statsEmbed.set_thumbnail(url="attachment://LogoNoBG.jpg")
    await Interaction.response.send_message(file=logo,embed=statsEmbed)

# Flood Command                                                                     
@tree.command(guild=discord.Object(id=serverID), name='flood', description='Sign off on an industrial quantity of ban appeals...')
async def new(Interaction: discord.Interaction, bool: Literal['ON', 'OFF']):
    if bool == 'OFF':
        print('OFF')
        offEmbed = discord.Embed(title="Kiwi's Mailbox Service", color=embedColor)
        offEmbed.add_field(name='Toggle OFF Option', value='This sub command has not been implemented yet.')
        offEmbed.set_thumbnail(url="attachment://LogoNoBG.jpg")
        await Interaction.response.send_message(file=logo,embed=offEmbed)
    if bool == 'ON':
        print('ON')
        status = discord.Embed(title= f'Kiwis Mailbox', description= f"**Status:** Active", color=embedColor)
        status.add_field(name="Form Type:", value="Ban Appeal")
        await Interaction.response.send_message(embed=status)
    
    while bool == 'ON':
        if bool == 'OFF':
            break
        dataProcessor.info()
        formInfo = discord.Embed(title='Kiwi Ban Form', description='', color=embedColor)
        formInfo.add_field(name='Discord Username and Tag',value=f'{dataProcessor.discordUsername}', inline=False)
        formInfo.add_field(name='Minecraft Username',value=f'{dataProcessor.ign}', inline=False)
        formInfo.add_field(name='Ban Reason',value=f'{dataProcessor.reason}', inline=False)
        getChannel = client.get_channel(feedbackChannel)
        await getChannel.send(embed=formInfo)

# Run
client.run(token)