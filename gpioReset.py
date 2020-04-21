import RPi.GPIO as GPIO
import time

relaypin = 7
GPIO.setmode(GPIO.BCM)
GPIO.setup(relaypin, GPIO.OUT)
GPIO.output(relaypin, GPIO.HIGH)
