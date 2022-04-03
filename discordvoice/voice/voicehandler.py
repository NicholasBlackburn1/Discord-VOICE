"""
voice handler class uwu

"""
from pyVoIP.VoIP import VoIPPhone, InvalidStateError



class voicehandler(object):


    # this is for the sip handler when some one dials the number
    def answer(call): # This will be your callback function for when you receive a phone call.
        try:
            call.answer()
            call.hangup()
        except InvalidStateError:
            pass