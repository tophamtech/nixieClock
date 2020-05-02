import transportController
import ledController
import tubeController
from datetime import datetime
import time

# Init
tubeController.writeDigit('----')
ledController.clearAll()


# tubeController.writeDigit('4276')

def tubeLeds():
    ledController.clearAll
    transportController.setTubeLed("northern")
    transportController.setTubeLed("jubilee")
    transportController.setTubeLed("central")


while 1 == 1:
    tubeController.writeDigit(datetime.now().strftime('%H%M'))
    tubeLeds()
    time.sleep(5)
    tubeController.writeDigit(transportController.busTimeToArrival())
    print('writing bus times')
    time.sleep(5)