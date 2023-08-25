#!/usr/bin/python
#
# Copyright (c) 2023
# All rights reserved.
#
# Auther : Shubham Mane
# Date Created : 12 August 2023
# Date Modified : 12 August 2023
#
# @Description : Demonstration of PWM on ESP32
# @file : PWM_LED.py (Changing the brightness of the LED)

from time import sleep
from machine import Pin, PWM

DUTY_MAX = 2**16 - 1

pwm = PWM(Pin(2), 100)
print(pwm)

while True:
   for i in range(0, DUTY_MAX):
        pwm.duty_u16(i)
        sleep(1/10000)
        
# End of script
