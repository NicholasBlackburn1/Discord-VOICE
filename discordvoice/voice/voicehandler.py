"""
voice handler class uwu

"""
import configparser
from re import S
import time
import wave
from pyVoIP.VoIP import VoIPPhone, InvalidStateError,InvalidStateError, CallState
from utils import consoleLog as log 
from pathlib import Path

class voicehandler(object):

    phone : VoIPPhone
    
    #this starts the voip connection
    def starting_connection(self,sipServer,sipPort,sipUser,sipPass,answer,ip):
        self.phone = VoIPPhone(sipServer, sipPort, sipUser, sipPass, callCallback=answer, myIP=ip)
        self.phone.start()

        # answers phone 


    # owo answes call
    def answer(self,call):
        try: 
            # this opens wave audio
            log.Warning("starting to read answer file")

            f = wave.open('announcment.wav', 'rb')
            frames = f.getnframes()
            data = f.readframes(frames)
            f.close()

            log.PipeLine_Ok("read file uwu")

            #awnsers call and writes the audio
            log.Warning("ansewerd call....")
            call.answer()

            log.Warning("writing audio.....")
            call.writeAudio(data) #This writes the audio data to the transmit buffer, this must be bytes.

            log.PipeLine_Ok("wrote audio to stream....")

            stop = time.time()+(frames/8000) #The number of frames/8000 is the length of the audio in seconds.

            # this will allow me to read 
            while time.time() <= stop and call.state == CallState.ANSWERED:

                time.sleep(1)

                # gets the data
                dtmf = call.getDTMF()
                if dtmf == "1":
                    log.Warning("connecting discord audio of main channel.....")

              

        except InvalidStateError:
            pass

        except:
            call.hangup()
