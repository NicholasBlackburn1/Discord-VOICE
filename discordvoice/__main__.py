"""
Main file uwu
"""

from utils import consoleLog as log


def main():
    log.PipeLine_init("starting...")


    log.Warning("Starting voip connection....")
    #TODO: add vip connection
    log.PipeLine_Ok("created voip connection...")
    

    log.Warning("starting discord bot.....")
    #TODO: add discord cliet int
    log.PipeLine_Ok("started discord bot")



if __name__ =='__main__':
    main()


