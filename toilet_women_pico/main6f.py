#6F women
import time
from machine import Pin,UART
import _thread

def sensor():
    toilet1=Pin(6, Pin.IN, Pin.PULL_DOWN)
    toilet2=Pin(7, Pin.IN, Pin.PULL_DOWN)
    toilet3=Pin(8, Pin.IN, Pin.PULL_DOWN)
    toilet4=Pin(9, Pin.IN, Pin.PULL_DOWN)

    led=Pin(25, Pin.OUT)
    led_panel=Pin(22, Pin.OUT)

    #TX to 5F TX=GP0/RX=GP1 baudrate11520
    uart = UART(0)

    while(True):
        led_panel.value(1)
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
        led_panel.value(0)
        time.sleep(1)


def receive():
    #RX from classroom TX=GP4/RX=GP5 baudrate11520
    uartrx = UART(1)

    led_6_1=Pin(2, Pin.OUT)
    led_6_2=Pin(3, Pin.OUT)
    led_5_1=Pin(10, Pin.OUT)
    led_5_2=Pin(11, Pin.OUT)
    led_5_3=Pin(12, Pin.OUT)
    led_5_4=Pin(13, Pin.OUT)
    led_4_1=Pin(14, Pin.OUT)
    led_4_2=Pin(15, Pin.OUT)
    led_3_1=Pin(16, Pin.OUT)
    led_3_2=Pin(17, Pin.OUT)
    led_3_3=Pin(18, Pin.OUT)
    led_3_4=Pin(19, Pin.OUT)
    led_2_1=Pin(20, Pin.OUT)
    led_2_2=Pin(21, Pin.OUT)

    led_6_1.value(0)
    led_6_2.value(0)
    led_5_1.value(0)
    led_5_2.value(0)
    led_5_3.value(0)
    led_5_4.value(0)
    led_4_1.value(0)
    led_4_2.value(0)
    led_3_1.value(0)
    led_3_2.value(0)
    led_3_3.value(0)
    led_3_4.value(0)
    led_2_1.value(0)
    led_2_2.value(0)


    while(True):
        if uartrx.any() > 0:
            all = str(uartrx.read(39)).strip("b\'\'")
            floor6_result = 0
            floor5_result = 0
            floor4_result = 0
            floor3_result = 0
            floor2_result = 0


            if all[0] == "1":
                all = int(all, 2)
                for i in range(1,38):
                    if all[38-i] == 1:
                        if 0<i:
                            if i<5:
                                floor6_result += 1
                        elif 5<i:
                            if i<17:
                                floor5_result += 1
                        elif 17<i:
                            if i<22:
                                floor4_result += 1
                        elif 22<i:
                            if i<34:
                                floor3_result += 1
                        elif 35<i:
                            floor2_result += 1

                #floor6 counter
                if floor6_result<4:
                    led_6_1.value(1)
                if floor6_result<2:
                    led_6_2.value(1)
                #floor4 counter
                if floor4_result<4:
                    led_4_1.value(1)
                if floor4_result<2:
                    led_4_2.value(1)
                #floor2 counter
                if floor2_result<4:
                    led_2_1.value(1)
                if floor2_result<2:
                    led_2_2.value(1)

                #floor5 counter
                if floor5_result<11:
                    led_5_1.value(1)
                if floor5_result<9:
                    led_5_2.value(1)
                if floor5_result<7:
                    led_5_3.value(1)
                if floor5_result<3:
                    led_5_4.value(1)

            #floor3 counter
                if floor3_result<11:
                    led_3_1.value(1)
                if floor6_result<9:
                    led_3_2.value(1)
                if floor3_result<7:
                    led_3_3.value(1)
                if floor3_result<3:
                    led_3_4.value(1)


                print(bin(all))

second_thread = _thread.start_new_thread(receive, ())

sensor()