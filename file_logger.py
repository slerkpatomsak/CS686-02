class file_logger:

    """
    Constructor
    """
    def __init__(self, log_level):
        self.__log_level__ = log_level


    """
    log
    Logs the message if log_level is less than or equal to
    the class' threshold. (In this case: does nothing.)
    """
    def log(self, log_level, message):
        if (log_level <= self.__log_level__ ):
            with open('file_log.txt', 'a') as file:
                file.write(str(log_level) + ": " +message+"\n")
                file.close()
        return
