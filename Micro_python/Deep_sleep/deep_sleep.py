#!/usr/bin/python
#
# Copyright (c) 2023
# All rights reserved.
#
# Author: Shubham Mane
# Date Created: 15 August 2023
# Date Modified: 15 August 2023
#
# Description: Demonstration of the Deep sleep on ESP32
# File: deep_sleep.py

import machine
from machine import Pin
from time import sleep

# Demonstration of Deep Sleep mode
print("---- Demonstration of Deep Sleep mode ----\n")

# Configure the GPIO 2 as Output
led_pin = Pin(2, Pin.OUT)

# Function definition ==> led_blink
def led_blink():
  for i in range(5):
    led_pin(1)
    print("LED ON")
    sleep(1)
    led_pin(0)
    print("LED OFF")
    sleep(1)

# led blink function call
led_blink()

# Entering into deep sleep for 10 seconds
print("Entering into deep sleep")
machine.deepsleep(10000)
print("done")

exit(0)

# End of script
