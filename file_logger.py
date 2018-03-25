from logger import logger

class file_logger(logger):

    def __init__(self, log_level):
        self.__log_level__ = log_level

    def log(self, log_level, message):
         if (log_level <= self.__log_level__ ):
            with open('file_log.txt', 'a') as file:
                file.write(str(log_level) + ": " +message+"\n")
                file.close()
