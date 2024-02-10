#!/usr/bin/python
#
# Copyright (c) 2023
# All rights reserved.
#
# Auther : Shubham Mane
# Date Created : 27 August 2023
# Date Modified : 27 August 2023
#
# @Description : Implementation of the UART2 on ESP32 in Micropython
# @file : UART2_ESP32.py

from machine import UART, Pin

# Configure the LED pin as out
led = Pin(2, Pin.OUT)

# Configure the UART0
# @brief - using UART0 and baud rate as 115200
uart_2 = UART(2, 115200)

# Initialization of UART0
uart_2_init = uart_2.init(115200, bits=8, parity=None, stop=1)
print(uart_2) # print configuration

# Instruction for UART 2
print("Press 'x' to turn LED ON & 'y' for to turn LED OFF on UART2")

# UART2 variable
rx_char = b''

while True:
  if uart_2.any() > 0:
    rx_char = uart_2.readline()
    if rx_char == b'x' or rx_char == b'X':
      uart_2.write('received character is - x\r\n')
      led.value(1)
      uart_2.write('LED ON!!!\r\n')
      print("LED ON!!!\n")
    elif rx_char == b'y' or rx_char == b'Y':
      uart_2.write('received character is - y\r\n')
      led.value(0)
      uart_2.write('LED OFF!!!\r\n')
      print("LED OFF!!!\n")
    else:
      uart_2.write('Please Enter the valid character')

exit(0)
            
# End of script
