#!/usr/bin/env python
import discord
from sys import exit

try:
    r = open('token.txt', 'r', encoding='UTF-8') #open token file
except FileNotFoundError:
    print("TOKEN.txtを作成しトークンを入力してください")
    exit(1)
data = r.read() #read token file
r.close() #close token file

TOKEN = data #TOKEN

bot = discord.Bot(activity=discord.Game("www")) #setting bot

bot.load_extension('commands') #load extension 

@bot.event
async def on_ready():
    print('接続しました')

bot.run(TOKEN) #launch bot