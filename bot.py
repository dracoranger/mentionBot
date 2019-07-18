#mentionBot
#By DracoRanger
import asyncio
import time
import discord
from discord.ext import commands

#import logging

client = discord.Client()
config = open('config.txt','r')
conf = config.readlines() #push to array or do directly
token = conf[0][:-1]
channelNum = int(conf[1][:-1])
target = int(conf[2][:-1])
timeBetween = int(conf[3][:-1])

@client.event
async def on_ready():
    global channelNum
    global target
    global timeBetween
    print('Logged in as ' + client.user.name)
    print(client.user.id)
    print('------')

    targetIs = client.get_user(target)
    print(targetIs)
    message = targetIs.mention + " is this annoying yet?"
    while(True):
        await client.get_channel(channelNum).send(message)
        time.sleep(timeBetween)


client.run(token)
