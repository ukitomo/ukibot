#!/usr/bin/env python
from aiohttp import connector
import discord
from time import sleep
from sys import exit

try:
    r = open('token.txt', 'r', encoding='UTF-8') #open token file
except FileNotFoundError:
    print("token.txtを作成しトークンを入力してください")
    exit(1)
data = r.read() #read token file
r.close() #close token file

TOKEN = data #TOKEN

bot = discord.Bot(activity=discord.Game("www")) #setting bot

bot.load_extension('commands') #load extension 

@bot.event
async def on_ready():
    print('接続しました')
while True:
    try:
        bot.run(TOKEN) #launch bot
    except connector.ClientConnectorError:
        sleep(5)
    except:
        break