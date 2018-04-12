from logger import logger

class stdout_logger(logger):

    def __init__(self,log_level):
        self.__log_level__ = log_level
        logger.__init__(self,log_level)


    def log(self, log_level, message):
         if (log_level <= self.__log_level__ ):
             print(str(log_level) + ": " +message)
