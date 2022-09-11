#6F women
import time
from machine import Pin,UART
import _thread

#toilet1=Pin(6, Pin.IN, Pin.PULL_DOWN)

def sensor():
    while(True):


def receive():
    while(True):
        all = str(uartrx.read(39)).strip("b\'\'")
        if all[0] == "1":
            all = int(all, 2)
            print(bin(all))

second_thread = _thread.start_new_thread(receive, ())

sensor()