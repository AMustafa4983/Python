import discord
import pandas as pd 
import numpy as np

client = discord.Client()
Token = "ODMzMzI2MjcyOTc2OTEyMzk0.YHwtkQ.hylpm7Uvxk8MjrwX884CNoeE-wE"
@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event 
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f"{username} : {user_message} ({channel})")
    
    if message.author == client.user :
        return
    if user_message.lower() == "hello" or user_message.lower() == "hlo" :
        await message.channel.send(f"blo {username}!")
        return
    elif user_message.lower() == "bye" :
        await message.channel.send(f"See you later {username}!")
        return

    if user_message.lower() == "die" :
        await message.channel.send(f"already broken!")
        await client.close()
        print("Bot Closed")

    if user_message.lower() == "ازيك" :
        await message.channel.send(f"الحمدلله انت عامل ايه")
        return



client.run(Token)