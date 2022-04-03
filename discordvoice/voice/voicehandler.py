"""
voice handler class uwu
TODO: get the path lib to work for the pith
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
    def starting_connection(self,sipServer,sipPort,sipUser,sipPass,ip):
        self.phone = VoIPPhone(sipServer, sipPort, sipUser, sipPass, callCallback=self.answer, myIP=ip)
        self.phone.start()

        # answers phone 


    # owo answes call
    def answer(self,call):
        try: 
            # this opens wave audio
            log.Warning("starting to read answer file")

            f = wave.open(str(Path().absolute())+"data/audio/"+'announcment.wav', 'rb')
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
                    #TODO: get discord connected to the voice audio


                if dtmf == "2":
                    log.Warning("connecting discord audio of game channel.....")
                    #TODO: get discord connected to the vgame 

                
                if dtmf == "3":
                    log.Warning("connecting discord audio of game channel.....")
                    #TODO: get discord connected to the vgame 

                else:
                    
                    log.Warning("Playing owo.... ")

                    f = wave.open(str(Path().absolute())+"data/audio/"+'owo.wav', 'rb')
                    frames = f.getnframes()
                    data = f.readframes(frames)
                    f.close()

                    log.Warning("writing audio.....")
                    call.writeAudio(data) #This writes the audio data to the transmit buffer, this must be bytes.

                    log.PipeLine_Ok("done playing audio ending call")

                    # should end call
                    if(time.time() <= stop and call.state == CallState.ANSWERED):
                        log.Warning("ending call")
                        call.hangup()
                        log.PipeLine_Ok("ended call.")




              

        except InvalidStateError:
            pass

        except:
            call.hangup()
