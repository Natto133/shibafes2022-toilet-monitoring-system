#5F men
import time
from machine import Pin,UART
import _thread

def sensor():
    toilet1=Pin(6, Pin.IN, Pin.PULL_DOWN)
    toilet2=Pin(7, Pin.IN, Pin.PULL_DOWN)
    toilet3=Pin(8, Pin.IN, Pin.PULL_DOWN)
    toilet4=Pin(9, Pin.IN, Pin.PULL_DOWN)
    toilet5=Pin(10, Pin.IN, Pin.PULL_DOWN)
    toilet6=Pin(11, Pin.IN, Pin.PULL_DOWN)

    led=Pin(25, Pin.OUT)

    #TX to 4F TX=GP0/RX=GP1 baudrate11520
    #RX from 6F TX=GP0/RX=GP1 baudrate11520
    uart = UART(0)

    while(True):
            
        #RX from 6F
        if uart.any() > 0:
            floor6 = str(uart.read(7)).strip("b\'\'")
            if floor6[0] != "1":
                continue
            floor6 = int(floor6, 2)
            print(bin(floor6))
            led.value(1)
            
            
            #check doors
            floor5 = 0b1
            
            floor5 = floor5 << 1
            floor5 = floor5 | toilet1.value()
            floor5 = floor5 << 1
            floor5 = floor5 | toilet2.value()
            floor5 = floor5 << 1
            floor5 = floor5 | toilet3.value()
            floor5 = floor5 << 1
            floor5 = floor5 | toilet4.value()
            floor5 = floor5 << 1
            floor5 = floor5 | toilet5.value()
            floor5 = floor5 << 1
            floor5 = floor5 | toilet6.value()
        
            print(bin(floor5))
            
            floor6 = floor6 << 7
            floorAll = floor6 | floor5
            print(bin(floorAll))
            uart.write('{:b}'.format(floorAll))
            
            led.value(0)

def receive():
    #RX from classroom TX=GP4/RX=GP5 baudrate11520
    uartrx = UART(1)
    while(True):
        if uartrx.any() > 0:
            all = str(uartrx.read(35)).strip("b\'\'")
            if all[0] == "1":
                all = int(all, 2)
                print(bin(all))

second_thread = _thread.start_new_thread(receive, ())

sensor()
