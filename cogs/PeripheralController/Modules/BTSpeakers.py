from cogs.PeripheralController.ModuleClass import Module
from cogs.PeripheralController.Enums.ModuleIdentifier import ModuleType
from cogs.PeripheralController.Enums.Status import Status
from typing import Any

class BTSpeakers(Module):
    '''
    This class is used to control the Bluetooth speakers connected to the computer.
    '''
    def __init__(self, name: str):
        super().__init__()
        self.type = ModuleType.SPEAKER
        self.name = name
        self.status = Status.CONNECTING

    def connect(self) -> bool:
        '''
        This method is used to connect to the Bluetooth speakers.
        '''
        self.status = Status.CONNECTED

    def disconnect(self) -> bool:
        '''
        This method is used to disconnect from the Bluetooth speakers.
        '''
        self.status = Status.DISCONNECTED

    def get_status(self) -> Status:
        '''
        This method is used to get the status of the Bluetooth speakers.
        '''
        return self.status

    def set_status(self, status: Status) -> bool:
        '''
        This method is used to set the status of the Bluetooth speakers.
        '''
        self.status = status

    def get_settings(self) -> dict[str, Any]:
        '''
        This method is used to get the settings of the Bluetooth speakers.
        '''
        return self.settings

    def set_settings(self, settings: dict[str, Any]) -> bool:
        '''
        This method is used to set the settings of the Bluetooth speakers.
        '''
        self.settings = settings

    def get_info(self) -> dict[str, Any]:
        '''
        This method is used to get the info of the Bluetooth speakers.
        '''
        return self.info    
    
    def get_volume(self) -> int:
        '''
        This method is used to get the volume of the Bluetooth speakers.
        '''
        return self.volume
    
    def set_volume(self, volume: int) -> bool:
        '''
        This method is used to set the volume of the Bluetooth speakers.
        '''