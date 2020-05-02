import requests
import json
from datetime import datetime
from time import mktime
import time
import ledController

busStopEndpoint = "https://api.tfl.gov.uk/StopPoint/490020143G/arrivals"
tubeStatusEndpoint = "https://api.tfl.gov.uk/line/mode/tube/status"

# Returns minutes until bus arrival, padded to 4 characters with 0's at the start
def busTimeToArrival():
    # Fetch from endpoint
    url = busStopEndpoint
    response = requests.request("GET", url)
    try:
        parsedData = json.loads(response.text)
        # Format date and find time between now and arrival
        formattedDate = time.strptime(parsedData[0]["expectedArrival"], '%Y-%m-%dT%H:%M:%SZ')
        formattedDateTime = datetime.fromtimestamp(mktime(formattedDate))
        difTime = formattedDateTime - datetime.utcnow()
        difMin = (difTime.total_seconds()/60)
        difMin = int(difMin)
        print('Time to arrival:')
        print(str(difMin))
        return str(difMin).zfill(4)
    except:
        # If error, display 9999
        return('9999')

# Returns status, from 0 (tube running fine) to 9 (tube with severe delays)
def tubeStatus(line):
    # Fetch from endpoint
    url = tubeStatusEndpoint
    response = requests.request("GET", url)
    try:
        parsedData = json.loads(response.text)
        for lineElement in parsedData:
            # Extract just status code
            if lineElement["id"] == line.lower():
                return (lineElement["lineStatuses"][0]["statusSeverity"])
    except:
        # Return error
        return(99)

def setTubeLed(line)
# Set which column the led should illuminate 
if line == 'northern':
    col = 1
elif line == 'jubilee':
    col = 2
elif line == 'central':
    col = 3

if tubeStatus(line) == 0:
    # show column green
    ledController.writeLed('green',col,'on')
elif 1 <= tubeStatus(line) <= 4:
    # show column orange
    ledController.writeLed('yellow',col,'on')
elif 5 <= tubeStatus(line) <=10:
    # show column red
    ledController.writeLed('red',col,'on')
else:
    # show blue if error
    ledController.writeLed('blue',col,'on')