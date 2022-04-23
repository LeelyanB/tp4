from cmath import log
from datetime import datetime
from email import message
from email.message import Message
from multiprocessing.connection import Client
from time import time
import discord
import datetime
from dotenv import load_dotenv
import os 



class MyBot(discord.Client,) :
    
    now =datetime.datetime.now()
    now = now.strftime("%m/%d/%y, :%H/%M/%S")
    now = str(now)

    async def on_ready(self):
      print("le bot est pret")

      with open("botlogs.txt", "a") as L :
        L.write(self.now +" bot connection\n")

    async def on_message(self,message):
       
       if message.content.startswith('hello'):
          await message.channel.send('Hello guy'.format(message)) 
       if  message.content.startswith('help'):
           await message.channel.send('write hello ')

       
       if message.author == self.user:
        with open("botlogs.txt", "a") as L :
            L.write( self.now +"message"+ message.content)
          
        

    async def on_member_join(member):
      general_channel: discord.TextChannel = client.get_channel(959385156123234352)
      await general_channel.send(content =f"Welcome!{ member.display_name}")
      

class token(fichier):
  
  def readtoken():
    with open("token.txt","r") as L:
      token= L.readline().rstrip()

    return token
    """
    async def log(self):
      await client.wait_until_ready()
      
       
      while not client.is_closed() :
         try :
           
           
          
             with open("botlogs.txt", "a") as L :

               if len(self.Connect) != 0:
                  L.write("Time :{int(time.time())},connection:{Connect.pop([0])}\n")

               if len(self.messageR) != 0:

                 L.write("Time :{int(time.time())},message:{messageR.pop([0])}\n")

               

         except Exception as b:
          
            print(b)  
     """
          







"""
class Log() :

  def __init__(self, fichier) :
      self.fichier = "Mylog"
   
  def message (self,message) :
    logger = logging.getlogger(self.fichier)
    logger.setlevel(logging.DEBUG)
    LB = logging.FileHandler(self.fichier)
    formatter = logging.Formatter('%(levelname)-15s %(asctime)s %(message)s')

    LB.setFormatter(formatter)
    LB.setlevel(logging.Debug)
    logger.info(message)
    
  def ErrorConnection(self) :

    logger = logging.getlogger(self.fichier)
    logger.setlevel(logging.DEBUG)
    LB = logging.FileHandler(self.fichier)
    formatter = logging.Formatter('%(levelname)-15s %(asctime)s %(message)s')
    LB.setFormatter(formatter)
    LB.setlevel(logging.Debug)
    logger.addHandler(LB)
    logger.error(" Connection error")
   """






client = MyBot()
load_dotenv(dotenv_path = "config")
token = token()
client.run(token.readtoken)
    
     