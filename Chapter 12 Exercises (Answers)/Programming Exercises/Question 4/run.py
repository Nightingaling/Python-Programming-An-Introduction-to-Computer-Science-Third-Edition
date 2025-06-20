from atm import ATM
from mainscreeninterface import MainScreenInterface
from identification import Identification

atm = ATM()
if atm.checkID(Identification()):
    interface = MainScreenInterface()
    atm.run(interface)
