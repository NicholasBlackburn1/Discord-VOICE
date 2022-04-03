"""
voice handler class uwu

"""
from pyVoIP.VoIP import VoIPPhone, InvalidStateError
from utils import consoleLog as log 


class voicehandler(object):

    phone : VoIPPhone

    # this is for the sip handler when some one dials the number
    def answer(self,call): # This will be your callback function for when you receive a phone call.
        try:
            call.answer()
            call.hangup()
        except InvalidStateError:
            pass
        
    # UwU starts the call
    def init_Call(self):
            log.Warning("Starting to connect to server.....")
            
            self.phone= VoIPPhone(<SIP Server IP>, <SIP Server Port>, <SIP Server Username>, <SIP Server Password>, callCallback=answer, myIP=<Your computers local IP>)
            self.phone.start()

