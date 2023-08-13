#!/usr/bin/python
#
# Copyright (c) 2023
# All rights reserved.
#
# Auther : Shubham Mane
# Date Created : 12 August 2023
# Date Modified : 12 August 2023
#
# @Description : TWI (I2C) Micro-python demonstration on ESP32 - WROOM 32
# @file : TWI.py

from machine import Pin, SoftI2C

SCL_PIN = Pin(23)
SDA_PIN = Pin(22)

i2c = SoftI2C(scl = SCL_PIN, sda = SDA_PIN , freq = 10000)

i2c_devices = i2c.scan()

if len(i2c_devices) == 0:
    print("No i2c device!!!")
else:
    print("i2c devices found : {0}".format(len(i2c_devices)))
    for device in i2c_devices:
        print("Device_address = {0}".format(hex(device)))

# End of script
