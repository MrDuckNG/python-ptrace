from ptrace.tools import minmax
from logging import ERROR, WARNING, INFO, DEBUG


def getLogFunc(logger, level):
    """
    Get the logger function for the specified logging level.
    """
    if level == ERROR or level not in [WARNING, INFO, DEBUG]:
        return logger.error
    elif level == WARNING:
        return logger.warning
    elif level == INFO:
        return logger.info
    else:
        return logger.debug


def changeLogLevel(level, delta):
    """
    Compute log level and make sure that the result is in DEBUG..ERROR.

    >>> changeLogLevel(ERROR, -1) == WARNING
    True
    >>> changeLogLevel(DEBUG, 1) == INFO
    True
    """
    return minmax(DEBUG, level + delta * 10, ERROR)
