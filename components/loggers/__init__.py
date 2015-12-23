## Import the available loggers.
from null.logger import NullLogger
from print2x.logger import Print2xLogger

## Define the available loggers.
__loggers = dict()
__loggers["null"] = NullLogger()
__loggers["print"] = Print2xLogger()

## Gets the names names of all available loggers.
def getAvailableLoggerNames():
    return __loggers.keys()

## Gets the desired logger if available.
def getLogger(loggerName):
    logger = None
    if loggerName in __loggers.keys():
        logger = __loggers[loggerName]
    return logger
