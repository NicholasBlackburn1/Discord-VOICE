"""
voice handler class uwu

"""
import configparser
from pyVoIP.VoIP import VoIPPhone, InvalidStateError
from utils import consoleLog as log 
from pathlib import Path

class voicehandler(object):

    phone : VoIPPhone
   
    # this is for the sip handler when some one dials the number
    def answer(self,call): # This will be your callback function for when you receive a phone call.
        try:
            call.answer()
            call.hangup()
        except InvalidStateError:
            pass
    
