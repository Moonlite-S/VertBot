from enum import Enum

class Status(Enum):
    '''
    This enum is used to represent the status of a peripheral.
    '''
    IDLE = "idle" # Also serves as the default status.
    CONNECTING = "connecting"
    DISCONNECTED = "disconnected"
    ERROR = "error"
    BUSY = "busy" # This is used when the peripheral is busy doing something.