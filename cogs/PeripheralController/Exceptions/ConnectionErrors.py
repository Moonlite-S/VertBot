
import logging

logger = logging.getLogger(__name__)

class PeripheralAlreadyConnectedError(Exception):
    '''
    This exception is raised when a peripheral is already connected.
    '''
    def __init__(self, message: str):
        super().__init__(message)
        logger.error(message)

class PeripheralNotConnectedError(Exception):
    '''
    This exception is raised when a peripheral is not connected.
    '''
    def __init__(self, message: str):
        super().__init__(message)
        logger.error(message)