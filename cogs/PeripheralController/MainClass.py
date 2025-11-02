from cogs.PeripheralController.Exceptions.ConnectionErrors import PeripheralAlreadyConnectedError, PeripheralNotConnectedError
from cogs.PeripheralController.ModuleClass import Module
import logging

logger = logging.getLogger(__name__)

class PeripheralController:
    '''
    This class is used to use set peripherals from the server for various commands.
    This higher level abstraction is used to make it easier to add new peripherals in the future in case I want to add more.

    Things I want to be able to do:
    - Have sub classes (modules) for each peripheral that can be used to control using this class. (That way I can add new peripherals in the future without having to change the main class.)
    - Have a a way to change settings for each peripheral. (For example, the Speaker TTS has a way to change the volume, the pitch, the speed, etc.)
    - Have a way to get the status of each peripheral. (For example, the Speaker TTS has a way to get the current volume, the pitch, the speed, etc.)

    The idea is to be able to use this class to control the peripherals without have to use the specific subclasses.

    Flow:
    - User uses a command from one of the cogs. (Example for the Speaker TTS)
    - The cog calls the PeripheralController class, initializes the speaker module (confirms it is connected to the computer)
    - The PC class then calls the speaker module to do the command. (Do the whole TTS process)
    - The PC class then returns the result to the cog.
    - The cog then sends the result to the user.
    '''

    def __init__(self):
        self.peripheral_list: list[Module] = []

    def list_peripherals(self) -> list[Module]:
        '''
        Lists all peripherals in the controller.
        '''
        return self.peripheral_list

    def list_all_peripherals(self) -> list[str]:
        '''
        Lists all available peripherals that can be added to the controller.
        '''
        return []

    def add_peripheral(self, peripheral: Module) -> Module:
        '''
        Adds a peripheral to the controller.
        
        Throws:
        - ConnectionError: If the peripheral is already connected.
        - DisconnectError: If the peripheral is not connected.
        - Exception: If there is an error connecting the peripheral.
        '''
        if peripheral in self.peripheral_list:
            raise PeripheralAlreadyConnectedError(f"Peripheral {peripheral.name} already exists.")
        
        try:
            if not peripheral.connect():
                raise PeripheralNotConnectedError(f"Error connecting peripheral: {peripheral.name}")

            self.peripheral_list.append(peripheral)
            return peripheral
        except (PeripheralNotConnectedError, PeripheralAlreadyConnectedError, Exception) as e:
            raise PeripheralNotConnectedError(f"Error connecting peripheral: {peripheral.name} - {e}")
        
    def remove_peripheral(self, chosen_peripheral: Module) -> None:
        '''
        Removes a peripheral from the controller.

        Needs to check if the peripheral is successfully removed.
        '''
        if not chosen_peripheral in self.peripheral_list:
            raise PeripheralNotConnectedError(f"Peripheral {chosen_peripheral.name} not found.")

        try:
            if not chosen_peripheral.disconnect():
                raise PeripheralNotConnectedError(f"Error disconnecting peripheral: {chosen_peripheral.name}")

            self.peripheral_list.remove(chosen_peripheral)
        except PeripheralNotConnectedError:
            raise PeripheralNotConnectedError(f"Error disconnecting peripheral: {chosen_peripheral.name}")
        except PeripheralNotConnectedError:
            raise PeripheralNotConnectedError(f"Peripheral {chosen_peripheral.name} not found.")

    
    