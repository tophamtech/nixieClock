# Tested, fully working 24/11/19

# newLed.writeLed('yellow',1,'off')

import smbus as smbus
bus = smbus.SMBus(1)
bus.write_byte_data(0x20, 0x00, 0x00)
bus.write_byte_data(0x20, 0x01, 0x00)
bus.write_byte_data(0x24, 0x00, 0x00)
bus.write_byte_data(0x24, 0x01, 0x00)
# # Turn on all red
# bus.write_byte_data(0x20, 0x15, 0xF0)
# # Turn on all yellow
# bus.write_byte_data(0x20, 0x15, 0x0F)
# # Turn on all green
# bus.write_byte_data(0x24, 0x15, 0xF0)
# # Turn on all blue
# bus.write_byte_data(0x24, 0x15, 0x0F)


def writeLed(colour, position, state):
    if colour == 'red':
        currentState = bin(bus.read_byte_data(0x20, 0x15))
        if position == 1:
            if state == 'on':
                bitmask = bin(int("11111110",2))
                futureState = int(currentState,2) & int(bitmask,2)
            if state == 'off':
                bitmask = bin(int("00000001",2))
                futureState = int(currentState,2) | int(bitmask,2)
        if position == 2:
            if state == 'on':
                bitmask = bin(int("11111101",2))
                futureState = int(currentState,2) & int(bitmask,2)
            if state == 'off':
                bitmask = bin(int("00000010",2))
                futureState = int(currentState,2) | int(bitmask,2)
        if position == 3:
            if state == 'on':
                bitmask = bin(int("11111011",2))
                futureState = int(currentState,2) & int(bitmask,2)
            if state == 'off':
                bitmask = bin(int("00000100",2))
                futureState = int(currentState,2) | int(bitmask,2)
        if position == 4:
            if state == 'on':
                bitmask = bin(int("11110111",2))
                futureState = int(currentState,2) & int(bitmask,2)
            if state == 'off':
                bitmask = bin(int("00001000",2))
                futureState = int(currentState,2) | int(bitmask,2)
        bus.write_byte_data(0x20, 0x15, futureState)
    elif colour == 'yellow':
        currentState = bin(bus.read_byte_data(0x20, 0x15))
        if position == 1:
            if state == 'on':
                bitmask = bin(int("11101111",2))
                futureState = int(currentState,2) & int(bitmask,2)
            if state == 'off':
                bitmask = bin(int("00010000",2))
                futureState = int(currentState,2) | int(bitmask,2)
        if position == 2:
            if state == 'on':
                bitmask = bin(int("11011111",2))
                futureState = int(currentState,2) & int(bitmask,2)
            if state == 'off':
                bitmask = bin(int("00100000",2))
                futureState = int(currentState,2) | int(bitmask,2)
        if position == 3:
            if state == 'on':
                bitmask = bin(int("10111111",2))
                futureState = int(currentState,2) & int(bitmask,2)
            if state == 'off':
                bitmask = bin(int("01000000",2))
                futureState = int(currentState,2) | int(bitmask,2)
        if position == 4:
            if state == 'on':
                bitmask = bin(int("01111111",2))
                futureState = int(currentState,2) & int(bitmask,2)
            if state == 'off':
                bitmask = bin(int("10000000",2))
                futureState = int(currentState,2) | int(bitmask,2)
        bus.write_byte_data(0x20, 0x15, futureState)
    if colour == 'green':
        currentState = bin(bus.read_byte_data(0x24, 0x15))
        if position == 1:
            if state == 'on':
                bitmask = bin(int("11110111",2))
                futureState = int(currentState,2) & int(bitmask,2)
            if state == 'off':
                bitmask = bin(int("00001000",2))
                futureState = int(currentState,2) | int(bitmask,2)
        if position == 2:
            if state == 'on':
                bitmask = bin(int("11111011",2))
                futureState = int(currentState,2) & int(bitmask,2)
            if state == 'off':
                bitmask = bin(int("00000100",2))
                futureState = int(currentState,2) | int(bitmask,2)
        if position == 3:
            if state == 'on':
                bitmask = bin(int("11111101",2))
                futureState = int(currentState,2) & int(bitmask,2)
            if state == 'off':
                bitmask = bin(int("00000010",2))
                futureState = int(currentState,2) | int(bitmask,2)
        if position == 4:
            if state == 'on':
                bitmask = bin(int("11111110",2))
                futureState = int(currentState,2) & int(bitmask,2)
            if state == 'off':
                bitmask = bin(int("00000001",2))
                futureState = int(currentState,2) | int(bitmask,2)
        bus.write_byte_data(0x24, 0x15, futureState)
    elif colour == 'blue':
        currentState = bin(bus.read_byte_data(0x24, 0x15))
        if position == 1:
            if state == 'on':
                bitmask = bin(int("01111111",2))
                futureState = int(currentState,2) & int(bitmask,2)
            if state == 'off':
                bitmask = bin(int("10000000",2))
                futureState = int(currentState,2) | int(bitmask,2)
        if position == 2:
            if state == 'on':
                bitmask = bin(int("10111111",2))
                futureState = int(currentState,2) & int(bitmask,2)
            if state == 'off':
                bitmask = bin(int("01000000",2))
                futureState = int(currentState,2) | int(bitmask,2)
        if position == 3:
            if state == 'on':
                bitmask = bin(int("11011111",2))
                futureState = int(currentState,2) & int(bitmask,2)
            if state == 'off':
                bitmask = bin(int("00100000",2))
                futureState = int(currentState,2) | int(bitmask,2)
        if position == 4:
            if state == 'on':
                bitmask = bin(int("11101111",2))
                futureState = int(currentState,2) & int(bitmask,2)
            if state == 'off':
                bitmask = bin(int("00010000",2))
                futureState = int(currentState,2) | int(bitmask,2)
        bus.write_byte_data(0x24, 0x15, futureState)

