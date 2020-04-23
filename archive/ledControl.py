import smbus as smbus
bus = smbus.SMBus(1)
bus.write_byte_data(0x20, 0x15, 0xFD)
print ~bus.read_byte_data(0x20, 0x15)



currentState = bin(bus.read_byte_data(0x20, 0x15))
print currentState
bitmask = bin(int("11111110",2))
print bitmask
futureState = int(currentState,2) & int(bitmask,2)
print bin(futureState)
bus.write_byte_data(0x20, 0x15, futureState)
