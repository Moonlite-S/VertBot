from cogs.PeripheralController.Exceptions.Disconnect import DisconnectError
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
        self.peripherals: list[Module] = []

    def add_peripheral(self, peripheral: Module) -> bool:
        '''
        Adds a peripheral to the controller.
        Returns True if the peripheral is added successfully, False otherwise.
        '''
        if peripheral in self.peripherals:
            logger.error(f"Peripheral {peripheral.name} already exists.")
            return False
        
        try:
            if peripheral.connect():
                self.peripherals.append(peripheral)
                return True
            else:
                logger.error(f"Error connecting peripheral: {peripheral.name}")
                return False
        except Exception as e:
            logger.error(f"Error connecting peripheral: {peripheral.name} - {e}")
            return False
        
    def remove_peripheral(self, chosen_peripheral: Module) -> bool:
        '''
        Removes a peripheral from the controller.
        Returns True if the peripheral is removed successfully, False otherwise.

        Needs to check if the peripheral is successfully removed.
        '''
        if chosen_peripheral in self.peripherals:
            try:
                if chosen_peripheral.disconnect():
                    self.peripherals.remove(chosen_peripheral)
                    return True
                else:
                    logger.error(f"Error disconnecting peripheral: {chosen_peripheral.name}")
                    return False
            except DisconnectError:
                logger.error(f"Error disconnecting peripheral: {chosen_peripheral.name}")
                return False
            except Exception:
                logger.error(f"Error removing peripheral: {chosen_peripheral.name}")
                return False

        return False
    