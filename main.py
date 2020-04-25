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


while 1 == 1:
    tubeController.writeDigit(datetime.now().strftime('%H%M'))
    tubeLeds()
    time.sleep(5000)
    tubeController.writeDigit(transportController.busTimeToArrival())
    print('writing bus times')
    time.sleep(5000)