#new change
import RPi.GPIO as GPIO
# Configure A-D pins for the 2x sn74141 chip
# These should be GPIO no not pin no
A1 = 18
B1 = 17
C1 = 27
D1 = 10

A2 = 9
B2 = 11
C2 = 5
D2 = 6

A3 = 7
B3 = 12
C3 = 16
D3 = 20

A4 = 13
B4 = 19
C4 = 26
D4 = 21

outputList = (A1,B1,C1,D1,A2,B2,C2,D2,A3,B3,C3,D3,A4,B4,C4,D4)
GPIO.setmode(GPIO.BCM)
GPIO.setup(outputList,GPIO.OUT)

# digits passed in as string. -(dash) if the tube should be off
def writeDigit(value):
    for i in range(4):
        targetValue = value[i:i+1]
        if targetValue == '-':
            displayDigit(i+1,"off")
        else:
            displayDigit(i+1, targetValue)


def displayDigit(tube, digit):
    print('tube - ',tube)
    print('digit', digit)
    if tube == 1:
        A = A1
        B = B1
        C = C1
        D = D1
    elif tube == 2:
        A = A2
        B = B2
        C = C2
        D = D2
    elif tube == 3:
        A = A3
        B = B3
        C = C3
        D = D3
    elif tube == 4:
        A = A4
        B = B4
        C = C4
        D = D4

    if digit == 0:
        print(A)
        GPIO.output(A,GPIO.LOW)
        GPIO.output(B,GPIO.LOW)
        GPIO.output(C,GPIO.LOW)
        GPIO.output(D,GPIO.LOW)
    elif digit == 1:
        GPIO.output(A,GPIO.HIGH)
        GPIO.output(B,GPIO.LOW)
        GPIO.output(C,GPIO.LOW)
        GPIO.output(D,GPIO.LOW)
    elif digit == 2:
        GPIO.output(A,GPIO.LOW)
        GPIO.output(B,GPIO.HIGH)
        GPIO.output(C,GPIO.LOW)
        GPIO.output(D,GPIO.LOW)
    elif digit == 3:
        GPIO.output(A,GPIO.HIGH)
        GPIO.output(B,GPIO.HIGH)
        GPIO.output(C,GPIO.LOW)
        GPIO.output(D,GPIO.LOW)
    elif digit == 4:
        GPIO.output(A,GPIO.LOW)
        GPIO.output(B,GPIO.LOW)
        GPIO.output(C,GPIO.HIGH)
        GPIO.output(D,GPIO.LOW)
    elif digit == 5:
        GPIO.output(A,GPIO.HIGH)
        GPIO.output(B,GPIO.LOW)
        GPIO.output(C,GPIO.HIGH)
        GPIO.output(D,GPIO.LOW)
    elif digit == 6:
        GPIO.output(A,GPIO.LOW)
        GPIO.output(B,GPIO.HIGH)
        GPIO.output(C,GPIO.HIGH)
        GPIO.output(D,GPIO.LOW)
    elif digit == 7:
        GPIO.output(A,GPIO.HIGH)
        GPIO.output(B,GPIO.HIGH)
        GPIO.output(C,GPIO.HIGH)
        GPIO.output(D,GPIO.LOW)
    elif digit == 8:
        GPIO.output(A,GPIO.LOW)
        GPIO.output(B,GPIO.LOW)
        GPIO.output(C,GPIO.LOW)
        GPIO.output(D,GPIO.HIGH)
    elif digit == 9:
        GPIO.output(A,GPIO.HIGH)
        GPIO.output(B,GPIO.LOW)
        GPIO.output(C,GPIO.LOW)
        GPIO.output(D,GPIO.HIGH)
    elif digit == "off":
        GPIO.output(A,GPIO.HIGH)
        GPIO.output(B,GPIO.HIGH)
        GPIO.output(C,GPIO.HIGH)
        GPIO.output(D,GPIO.HIGH)




