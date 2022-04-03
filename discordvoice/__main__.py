"""
Main file uwu
"""

import configparser
from pathlib import Path
from voice.voicehandler import voicehandler
from utils import consoleLog as log
import socket

def main():
    log.Warning("reading config...")

    log.PipeLine_Data( "this is the config path"+" "+ str(Path().absolute())+"/data/Config.ini")

    config = configparser.ConfigParser(str(Path().absolute())+"/data/Config.ini")

    # server ip and port 
    serverip = config.get['sip_server']
    serverport = int(config.get['sip_server_port'])

    #sip user and pas
    sipuser =  str(config.get['sip_username'])
    sippass = str(config.get['sip_password'])

    # gets server ip

    h_name = socket.gethostname()
    IP_addres = socket.gethostbyname(h_name)


    log.PipeLine_init("starting...")

    # handled discord client connection
    log.Warning("starting discord bot.....")
    #TODO: add discord cliet int
    log.PipeLine_Ok("started discord bot")

    # connects the voice server
    log.Warning("Starting voip connection....")
    #TODO: add vip connection
    
    # this is the voip server connection
    voicehandler.starting_connection(voicehandler,serverip,serverport,sipuser,sippass,IP_addres)
    
    log.PipeLine_Ok("created voip connection...")
    



if __name__ =='__main__':
    main()


