import transportController
import ledController
# import tubeController
from datetime import datetime
import time


while 1 == 1:
    print(datetime.now().strftime('%H%M'))
    tubeLeds
    time.sleep(10000)


# tubeController.writeDigit('4276')

def tubeLeds():
    northernStatus = transportController.tubeStatus("northern")
    jubileeStatus = transportController.tubeStatus("jubilee")
    if northernStatus == 0:
        # show first column green
        ledController.writeLed('green',1,'on')
    elif 1 <= northernStatus <= 4:
        # show first column orange
        ledController.writeLed('yellow',1,'on')
    else:
        # show first column red
        ledController.writeLed('red',1,'on')