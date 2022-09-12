#3F men
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

    #TX to 2F TX=GP0/RX=GP1 baudrate11520
    #RX from 4F TX=GP0/RX=GP1 baudrate11520
    uart = UART(0)

    while(True):    
        #RX from 4F
        if uart.any() > 0:
            floor4 = str(uart.read(21)).strip("b\'\'")
            if floor4[0] != "1":
                continue
            floor4 = int(floor4, 2)
            print(bin(floor4))
            led.value(1)
            
            
            #check doors
            floor3 = 0b1
            
            floor3 = floor3 << 1
            floor3 = floor3 | toilet1.value()
            floor3 = floor3 << 1
            floor3 = floor3 | toilet2.value()
            floor3 = floor3 << 1
            floor3 = floor3 | toilet3.value()
            floor3 = floor3 << 1
            floor3 = floor3 | toilet4.value()
            floor3 = floor3 << 1
            floor3 = floor3 | toilet5.value()
            floor3 = floor3 << 1
            floor3 = floor3 | toilet6.value()
        
            print(bin(floor3))
            
            floor4 = floor4 << 7
            floorAll = floor4 | floor3
            print(bin(floorAll))
            uart.write('{:b}'.format(floorAll))
        
            led.value(0)



def receive():
    #RX from classroom TX=GP4/RX=GP5 baudrate11520
    uartrx = UART(1)
    while(True):
        all = str(uartrx.read(35)).strip("b\'\'")
        if all[0] == "1":
            all = int(all, 2)
            print(bin(all))

second_thread = _thread.start_new_thread(receive, ())

sensor()