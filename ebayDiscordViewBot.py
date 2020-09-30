import discord
import os
import webbrowser
import selenium
import time
from selenium import webdriver

client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    # driver = webdriver.Ie('c:\\program files\\internet explorer\\iexplore.exe')
    
    # driver.get('https://www.chegg.com/homework-help/questions-and-answers/cash-check-bank-teller-accidentally-switches-dollars-cents-amount-given-47-cents-twice-cor-q23667407')

    # driver.maximize_window()

    

@client.event
async def on_message(message):
    #check that the bot is not calling itself
    if message.author == client.user:
        return

    if message.content.startswith('https://www.ebay'): #change this at some point to say blessme then use the link 
        webbrowser.open(message.content, new=2)
        #await message.channel.send('do ur hw fool')
        await message.channel.send(file=discord.File('cheggImage.png'))
    if message.content.startswith('!status'): #change this at some point to say blessme then use the link 
        webbrowser.open(message.content, new=2)
        #await message.channel.send('do ur hw fool')
        await message.channel.send("ONLINE")
client.run('PD5izQ9x0QS-yf9kfybdFlQeBq1QPagm')

#Backlog
    #use diff browser
    #handle dms
    #close browser
    #run on server