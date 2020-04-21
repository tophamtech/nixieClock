import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
myList = (2,4)
GPIO.setup(myList,GPIO.OUT)
print "LED OFF"
GPIO.output(2,GPIO.LOW)
