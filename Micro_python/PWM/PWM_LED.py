#!/usr/bin/python
#
# Copyright (c) 2023
# All rights reserved.
#
# Auther : Shubham Mane
# Date Created: 12 August 2023
# Date Modified: 12 August 2023
#
# Description: Demonstration of PWM on ESP32
# File : PWM_LED.py (Changing the brightness of the LED)

from time import sleep
from machine import Pin, PWM

# Max duty cycle
MAX_DUTY_CYCLE = 65535

# Count variable
count = 0

# PWM Configuration
pwm = PWM(Pin(2), 100)  # configure the frequency as 100Hz
print(pwm, "\n")

while True:
  print("Brightness increasing...")
  for x in range(0, MAX_DUTY_CYCLE):
    pwm.duty_u16(x)
    sleep(1 / 10000)
  print("Brightness decreasing...")
  for y in range(MAX_DUTY_CYCLE, 0, -1):
    pwm.duty_u16(y)
    sleep(1 / 10000)
  print("Count = {0}\n".format(count))
  count = count + 1

exit(0)

# End of script
