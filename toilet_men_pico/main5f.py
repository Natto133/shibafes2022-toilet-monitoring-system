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
    led_panel=Pin(22, Pin.OUT)

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
            led_panel.value(1)
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

    led_6_1=Pin(2, Pin.OUT)
    led_6_2=Pin(3, Pin.OUT)
    led_6_3=Pin(12, Pin.OUT)
    led_5_1=Pin(13, Pin.OUT)
    led_5_2=Pin(14, Pin.OUT)
    led_5_3=Pin(15, Pin.OUT)
    led_4_1=Pin(16, Pin.OUT)
    led_4_2=Pin(17, Pin.OUT)
    led_4_3=Pin(18, Pin.OUT)
    led_3_1=Pin(19, Pin.OUT)
    led_3_2=Pin(20, Pin.OUT)
    led_3_3=Pin(21, Pin.OUT)
    led_2_1=Pin(26, Pin.OUT)
    led_2_2=Pin(27, Pin.OUT)
    led_2_3=Pin(28, Pin.OUT)

    led_6_1.value(0)
    led_6_2.value(0)
    led_6_3.value(0)
    led_5_1.value(0)
    led_5_2.value(0)
    led_5_3.value(0)
    led_4_1.value(0)
    led_4_2.value(0)
    led_4_3.value(0)
    led_3_1.value(0)
    led_3_2.value(0)
    led_3_3.value(0)
    led_2_1.value(0)
    led_2_2.value(0)
    led_2_3.value(0)


    while(True):
        if uartrx.any() > 0:
            all = str(uartrx.read(35)).strip("b\'\'")
            floor6_result = 0
            floor5_result = 0
            floor4_result = 0
            floor3_result = 0
            floor2_result = 0


            if all[0] == "1":
                all = int(all, 2)
                for i in range(1,34):
                    if all[38-i] == 1:
                        if 0<i:
                            if i<7:
                                floor6_result += 1
                        elif 7<i:
                            if i<14:
                                floor5_result += 1
                        elif 14<i:
                            if i<21:
                                floor4_result += 1
                        elif 21<i:
                            if i<28:
                                floor3_result += 1
                        elif 28<i:
                            floor2_result += 1

            # floor6 counter
                if floor6_result<6:
                    led_6_1.value(1)
                if floor6_result<4:
                    led_6_2.value(1)
                if floor6_result<2:
                    led_6_3.value(1)


            # floor5 counter
                if floor5_result<6:
                    led_5_1.value(1)
                if floor5_result<4:
                    led_5_2.value(1)
                if floor5_result<2:
                    led_5_3.value(1)


            # floor4 counter
                if floor4_result<6:
                    led_4_1.value(1)
                if floor4_result<4:
                    led_4_2.value(1)
                if floor4_result<2:
                    led_4_3.value(1)


            # floor3 counter
                if floor3_result<6:
                    led_3_1.value(1)
                if floor3_result<4:
                    led_3_2.value(1)
                if floor3_result<2:
                    led_3_3.value(1)


            # floor2 counter
                if floor2_result<6:
                    led_2_1.value(1)
                if floor2_result<4:
                    led_2_2.value(1)
                if floor2_result<2:
                    led_2_3.value(1)


                print(bin(all))

second_thread = _thread.start_new_thread(receive, ())

sensor()
