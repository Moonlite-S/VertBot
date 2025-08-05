from abc import ABC, abstractmethod
from typing import Any
from cogs.PeripheralController.Enums.ModuleIdentifier import ModuleType
from cogs.PeripheralController.Enums.Status import Status

class Module(ABC):
    '''
    This class is used as the base class for all the modules. (Each module is a peripheral that can be controlled.)

    This class features some basic methods that all modules should have.
    - connect: This method is used to connect to the peripheral.
    - disconnect: This method is used to disconnect from the peripheral.
    - get_status: This method is used to get the status of the peripheral.
    - set_status: This method is used to set the status of the peripheral.
    - get_settings: This method is used to get the settings of the peripheral.
    - set_settings: This method is used to set the settings of the peripheral.
    - get_info: This method is used to get the info of the peripheral.
    '''

    def __init__(self):
        ''' These properties are shared by all modules. '''
        self.type: ModuleType = None # This is the type of the module.
        self.status = Status.IDLE
        self.settings: dict[str, Any] = {} 

    @abstractmethod
    def connect(self) -> bool:
        '''
        Verifies and connects to the peripheral.
        Returns True if the connection is successful, False otherwise.
        '''
        pass

    @abstractmethod
    def disconnect(self) -> bool:
        '''
        Disconnects from the peripheral.
        Returns True if the disconnection is successful, False otherwise.
        '''
        pass

    @abstractmethod
    def get_status(self) -> Status:
        '''
        Gets the status of the peripheral.
        Returns the status of the peripheral.
        '''
        pass

    @abstractmethod
    def set_status(self, status: Status) -> bool:
        '''
        Sets the status of the peripheral.
        Returns True if the status is set successfully, False otherwise.
        '''
        pass

    @abstractmethod
    def get_settings(self) -> dict[str, Any]:
        '''
        Gets the settings of the peripheral.
        Returns the settings of the peripheral.
        '''
        pass

    @abstractmethod
    def set_settings(self, settings: dict[str, Any]) -> bool:
        '''
        Sets the settings of the peripheral.
        Returns True if the settings are set successfully, False otherwise.
        '''
        pass

    @abstractmethod
    def get_info(self) -> dict[str, Any]:
        '''
        Gets the info of the peripheral.
        Returns the info of the peripheral.
        '''
        pass