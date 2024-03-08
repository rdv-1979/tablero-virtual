import pyfirmata
import time

comport = 'COM4'

board = pyfirmata.Arduino(comport)

led_1 = board.get_pin('d:9:o')
servo_1 = board.get_pin('d:10:s')
rele_1 = board.get_pin('d:8:o')

rele_1.write(0)
def led(total):
    if total == 0:
        led_1.write(0)

    elif total == 1:
        led_1.write(1)

def servo(total):
    if total == 0:
        servo_1.write(45)

    elif total == 1:
        servo_1.write(150)

def rele(total):
    if total == 0:
        rele_1.write(0)

    elif total == 1:
        rele_1.write(1)

