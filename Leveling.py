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


TOKEN = 'ODQ3ODczMjMzNjA4NTA3NDUy.YLEZew.QAFnmsfNb_5Uu-WSzKza9VKGc4g'

bot = commands.Bot(command_prefix='-')



@bot.event
async def on_member_join(member):
    with open('user.json', 'r') as f:
        users = json.load(f)

    await update_data(users, member)

    with open ('users.json', 'w') as f:
        json.dump(users, f)

@bot.event
async def on_message(message):
    with open('users.json', 'r') as f:
        users = json.load(f)

    await update_data(users, message.author)
    await add_experience(users, message.author, 5)
    await level_up(users, message.author, message.channel)

    with open ('users.json', 'w') as f:
        json.dump(users, f)
        
async def update_data(users, user):
    if not user.id in users:
        users['user.id'] = {}
        users['user.id']['experience'] = 0
        users['user.id']['level'] = 1

async def add_experience(users, user, exp):
    users['user.id']['experience'] += exp

async def level_up(users, user, channel):
    experience = users['user.id']['experience']
    lvl_start = users['user.id']['level']
    lvl_end = int(experience ** (1/4))

    if lvl_start < lvl_end:
        await bot.send_message(channel, '{} ist auf level {} aufgestiegen.'.format(user.mention, lvl_end))
        user['user.id']['level'] = lvl_end

bot.run(TOKEN, bot=True)