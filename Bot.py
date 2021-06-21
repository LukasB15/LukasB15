# IMPORT
import asyncio
from collections import Counter
from itertools import count
from logging import Logger
from time import sleep
import discord
from discord import message
from discord import Member
from discord import embeds
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands.core import bot_has_permissions, has_permissions
import json
import os
import random

TOKEN = 'ODQ3ODczMjMzNjA4NTA3NDUy.YLEZew.QAFnmsfNb_5Uu-WSzKza9VKGc4g'

bot = commands.Bot(command_prefix='-')

os.chdir(r'C:\Users\Lukas\Downloads\Discord-Bot')



#EVENTS



@bot.event
async def on_ready():
    print('Ready...')
    bot.loop.create_task(status_task())

    channel = bot.get_channel(851107497006727181)
    msg = await channel.send("Der Bot ist Online")
        



@bot.event
async def status_task():
    while True:
        await bot.change_presence(activity=discord.Game('Lukas#5134'), status=discord.Status.online)
        await asyncio.sleep(20)
        await bot.change_presence(activity=discord.Game('Version 0.2'), status=discord.Status.online)
        await asyncio.sleep(20)
        await bot.change_presence(activity=discord.Game('-Hilfe'), status=discord.Status.online)
        await asyncio.sleep(20)
        
#commands
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=0):
    
    if amount > 100:

        await ctx.send("Tut mir Leid, ich kann maximal **100** Nachrichten löschen.")

    if amount <= 100:
            
            await ctx.channel.purge(limit=amount + 1)
            embed = discord.Embed(
            title="clear-command",
            description=f"ich habe {amount} Nachrichten erfolgreich gelöscht",
            color=discord.Color.red())
        
            await ctx.send(embed=embed, delete_after=3.5)

@bot.command(aliases=['boot'])
async def kick(ctx, member:discord.Member, *, reason=None):
     await member.kick(reason=reason)
     await ctx.send(f'{member.mention} wurde gekickt')

@bot.command(aliases=['hammer'])
async def ban(ctx, member:discord.Member, *, reason=None):
     await member.ban(reason=reason)
     await ctx.send(f'{member.mention} wurde gebannt')
     
@bot.command(aliases=['vergeben'])
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('-')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discimnator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.mention} wurde entbannt')
            return


@bot.command(name='Hilfe')
async def help(context):
    HilfeEmbed = discord.Embed(title="**Hilfe**", description="Das sind alle Commands für den Bot", color=0x00ff00)
    HilfeEmbed.add_field(name="-help: ", value="Zeigt diese Hilfe an", inline=False)
    HilfeEmbed.add_field(name="-version", value="Zeigt die Version des Bots an", inline=False)
    HilfeEmbed.add_field(name="-clear <Zahl>", value="Löscht Nachrichten im Aktuellem Channel", inline=False)
    HilfeEmbed.add_field(name="-kick/-boot <name> <grund>", value="Dadurch wird eine Person vom Server gekickt", inline=False)
    HilfeEmbed.add_field(name="-8b/-8ball <Frage>", value="Antwortet der Bot auf eine Zuffälige Frage", inline=False)
    HilfeEmbed.set_footer(text="YEEEEEET")
    HilfeEmbed.set_author(name="Lukas")

    await context.message.channel.send(embed=HilfeEmbed)

@bot.command(name='version')
async def version(context):
    VersionEmbed = discord.Embed(title="Current Version", description="The Bot is in Version 0.2", color=0x00ff00)
    VersionEmbed.add_field(name="Version Code:", value="v0.2.0", inline=False)
    VersionEmbed.add_field(name="Date Released:", value="June 5th, 2021", inline=False)
    VersionEmbed.set_footer(text="YEEEEEET")
    VersionEmbed.set_author(name="Lukas")   
   
    await context.message.channel.send(embed=VersionEmbed)

@bot.command(aliases=['p'])
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command(aliases=['8ball', '8b'])
async def eightball(ctx, *, question):
    responses = ["Es ist sicher.",
                "Es ist Eindeutig so.",
                "ohne zweifel.",
                "Ja - definitiv",
                "Du kannst dich drauf verlassen.",
                "aus meiner Sicht, ja.",
                "Höchstwahrscheinlich.",
                "Es sieht gut aus.",
                "Ja.",
                "Anscheinend schon.",
                "Antwort unscharf, versuch es erneut.",
                "Keine Ahnung.",
                "Am bessten sage ich es nicht jetzt.",
                "Kann ich jetzt noch nicht sagen.",
                "Konzentrieren und nochmal fragen.",
                "Verlass dich nicht drauf.",
                "Meine Antwort ist Nein.",
                "Meine Quellen sagen nein.",
                "Sieht nicht gut aus",
                "Sehr Zweifelhaft."]



    await ctx.send(f':8ball: Question: {question}\n:8ball: Answer: {random.choice(responses)}')

bot.run(TOKEN, bot=True)