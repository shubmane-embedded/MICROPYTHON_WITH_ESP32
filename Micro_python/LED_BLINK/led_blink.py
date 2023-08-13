#!/usr/bin/python
#
# Copyright (c) 2023
# All rights reserved.
#
# Auther : Shubham Mane
# Date Created : 12 August 2023
# Date Modified : 12 August 2023
#
# @Description : first Micro-python demonstration on ESP32 - WROOM 32
# @file : led_blink.py

from machine import Pin
from time import sleep

print("----First ESP32 WROOM 32 with Micropython----")
print("----LED Blink on GPIO 2 on ESP32 WROOM 32----\n")
print("------------Blinking LED  7 times------------\n")

#variable
count = 0

led = Pin(2, Pin.OUT)

while True:
    led.value(1)
    print("STATUS - LED ON")
    sleep(1)
    led.value(0)
    print("STATUS - LED OFF")
    sleep(1)
    # count increment
    count = count + 1
    print("count = {0}\n".format(count))
    # checking for count
    if count == 7:
        print("Done!!! Exiting\n")
        break

# End of script
