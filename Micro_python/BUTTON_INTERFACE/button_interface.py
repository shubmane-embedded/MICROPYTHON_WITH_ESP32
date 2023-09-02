#!/usr/bin/python
#
# Copyright (c) 2023
# All rights reserved.
#
# Auther : Shubham Mane
# Date Created : 2nd Sept 2023
# Date Modified : 2nd Sept 2023
#
# @Description : Interfacing button with ESP32 in Micropython
# @file : button_interface.py

from machine import Pin
from time import sleep

# Variable to store the LED status
LED_STATUS = 0  # 0 ==> LED OFF, 1 ==> LED ON

# LED configuration
LED = Pin(2, Pin.OUT)
print(LED)

# BUTTON configuration
BUTTON = Pin(16, Pin.IN, Pin.PULL_UP)
print(BUTTON)

# Press the button on GPIO 25
print("Press the button to turn LED ON/OFF on GPIO 2")

# Initially keeping the LED OFF
print("Initially LED is OFF\n")
LED.value(0)

while True:
    if LED_STATUS == 0 and BUTTON.value() == 0:
        print("LED ON!!!")
        LED.value(1)
        LED_STATUS = 1 # LED is in ON state
        sleep(0.5)
    if LED_STATUS == 1 and BUTTON.value() == 0:
        print("LED OFF!!!")
        LED.value(0)
        LED_STATUS = 0 # LED is in OFF status
        sleep(0.5)

# End of script
