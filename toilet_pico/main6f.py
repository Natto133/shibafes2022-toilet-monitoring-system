#6F women
import time
from machine import Pin,UART
import _thread

toilet1=Pin(6, Pin.IN, Pin.PULL_DOWN)
toilet2=Pin(7, Pin.IN, Pin.PULL_DOWN)
toilet3=Pin(8, Pin.IN, Pin.PULL_DOWN)
toilet4=Pin(9, Pin.IN, Pin.PULL_DOWN)

led=Pin(25, Pin.OUT)

#TX to 5F
uart = UART(0)

uartrx = UART(1)


def sensor():
    while(True):
        led.value(1)
        floor6 = 0b1
        
        floor6 = floor6 << 1
        floor6 = floor6 | toilet1.value()
        floor6 = floor6 << 1
        floor6 = floor6 | toilet2.value()
        floor6 = floor6 << 1
        floor6 = floor6 | toilet3.value()
        floor6 = floor6 << 1
        floor6 = floor6 | toilet4.value()
        
        print(bin(floor6))
        
        uart.write('{:b}'.format(floor6))
        
        led.value(0)
        time.sleep(1)


def receive():
    while(True):
        all = str(uartrx.read(39)).strip("b\'\'")
        if all[0] == "1":
            all = int(all, 2)
            print(bin(all))
        time.sleep(0.1)

second_thread = _thread.start_new_thread(receive, ())

sensor