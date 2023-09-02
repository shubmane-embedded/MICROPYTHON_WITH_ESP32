#!/usr/bin/python
#
# Copyright (c) 2023
# All rights reserved.
#
# Auther : Shubham Mane
# Date Created : 15 August 2023
# Date Modified : 15 August 2023
#
# @Description : Demonstration of the Deep sleep on ESP32
# @file : deep_sleep.py

import machine
from machine import Pin
from time import sleep

print("----Demonstration of Deep Sleep mode----\n")

led_pin = Pin(2, Pin.OUT)

def led_blink():
    for i in range(5):
        led_pin(1)
        print("LED ON")
        sleep(1)
        led_pin(0)
        print("LED OFF")
        sleep(1)

led_blink()

print("Entering into deep sleep")
machine.deepsleep(10000)
print("done")

exit(0)

# End of script
