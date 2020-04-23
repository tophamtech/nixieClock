import requests
import json
from datetime import datetime
from time import mktime
import time

def busTimeToArrival():
    url = "https://api.tfl.gov.uk/StopPoint/490020143G/arrivals"
    response = requests.request("GET", url)
    parsedData = json.loads(response.text)

    formattedDate = time.strptime(parsedData[0]["expectedArrival"], '%Y-%m-%dT%H:%M:%SZ')
    formattedDateTime = datetime.fromtimestamp(mktime(formattedDate))
    difTime = formattedDateTime - datetime.utcnow()
    difMin = (difTime.total_seconds()/60)
    difMin = int(difMin)
    return difMin

def tubeStatus(line):
    url = "https://api.tfl.gov.uk/line/mode/tube/status"
    response = requests.request("GET", url)
    parsedData = json.loads(response.text)
    for lineElement in parsedData:
        if lineElement["id"] == line.lower():
            return (lineElement["lineStatuses"][0]["statusSeverity"])

print(busTimeToArrival())
print tubeStatus("northern")
print tubeStatus("jubilee")