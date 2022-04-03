"""
this is for handling my discord client 
"""


import discord
from ext.voice_recv import voice_client
from ext.voice_recv.reader import AudioSink

from ext import voice_recv
import consoleLog as log 

class MyClient(discord.Client):

    audio : AudioSink

    def callback(member, packet):
        log.info(str(member) + " "+ str(packet))

    async def on_ready(self):
        log.Warning('Logged on as'+ str(self.user))
        

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')


        if message.content == '!about':
            await message.channel.send('this is a test bot for nicky blackburns voip to discord call bot ') 


        if message.content == '!connect':
     
            await message.channel.send('conncting to vc ✅ ') 
            vc = await voice_recv.VoiceRecvClient.voice_connect(message.author.voice.channel.connect)
         
    
            log.PipeLine_Data("audio data"+ " "+ str(data))



intents = discord.Intents.all()
client = MyClient(intents=intents)
