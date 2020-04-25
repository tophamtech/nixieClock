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
    northernStatus = transportController.tubeStatus("northern")
    jubileeStatus = transportController.tubeStatus("jubilee")
    centralStatus = transportController.tubeStatus("central")
    ledController.clearAll
    if northernStatus == 0:
        # show first column green
        ledController.writeLed('green',1,'on')
    elif 1 <= northernStatus <= 4:
        # show first column orange
        ledController.writeLed('yellow',1,'on')
    else:
        # show first column red
        ledController.writeLed('red',1,'on')
    if jubileeStatus == 0:
        # show first column green
        ledController.writeLed('green',2,'on')
    elif 1 <= jubileeStatus <= 4:
        # show first column orange
        ledController.writeLed('yellow',2,'on')
    else:
        # show first column red
        ledController.writeLed('red',2,'on')
    if centralStatus == 0:
        # show first column green
        ledController.writeLed('green',3,'on')
    elif 1 <= centralStatus <= 4:
        # show first column orange
        ledController.writeLed('yellow',3,'on')
    else:
        # show first column red
        ledController.writeLed('red',3,'on')


while 1 == 1:
    tubeController.writeDigit(datetime.now().strftime('%H%M'))
    tubeLeds()
    time.sleep(5)
    tubeController.writeDigit(transportController.busTimeToArrival())
    print('writing bus times')
    time.sleep(5)