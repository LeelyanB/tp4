from cmath import log
from datetime import datetime
from email import message
from email.message import Message
from multiprocessing.connection import Client
from time import time
import discord
import datetime
import os 
from  dotenv import load_dotenv



class MyBot(discord.Client,) :
    
    now =datetime.datetime.now()
    now = now.strftime("%m/%d/%y, :%H:%M:%S")
    now = str(now)

    async def on_ready(self):
      print("le bot est pret")

      with open("botlogs.txt", "a") as L :
        L.write(self.now +" bot connection\n")

    async def on_message(self,message):
       
       if message.content.startswith('hello'):
          await message.channel.send('Hello dude'.format(message))  
       
       if message.author == self.user:
        with open("botlogs.txt", "a") as L :
            L.write( self.now +"message "+ message.content)
            
       if  message.content.startswith('help'):
          await message.channel.send('write hello ')    
          
        

    async def on_member_join(member):
      general_channel: discord.TextChannel = client.get_channel(959385156123234352)
      await general_channel.send(content =f"Welcome!{ member.display_name}")
      





load_dotenv(dotenv_path="config")
client = MyBot()
client.run(os.getenv("token"))
    
     
