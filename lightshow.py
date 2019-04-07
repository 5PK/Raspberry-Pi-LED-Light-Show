import os
import sys
import tty
import time

from threading import Thread

import RPi.GPIO as GPIO
import random

import pyaudio
from struct import unpack
# import audioop
import numpy as np

import wave


from getbpm import get_file_bpm



# Pins to use
# 7, 1, 8

#################
#   GPIO SETUP  #
#################

# Turn off warnings
GPIO.setwarnings(False)

# Set pin mapping to board, use GPIO numbers not pin numbers
GPIO.setmode(GPIO.BCM)


class Pin(object):
    def __init__(self, pin_number):
        self.pin_number = pin_number

RED = Pin(pin_number=7)
GREEN = Pin(pin_number=1)
BLUE = Pin(pin_number=8)

pins = [RED, GREEN, BLUE]

pin_numbers = [pin.pin_number for pin in pins]

# GPIO.LOW = relay on, GPIO.HIGH = relay off
on = lambda pin: GPIO.output(pin, 1)
off = lambda pin: GPIO.output(pin, 0)

# set up each pin
for pin in pin_numbers:
    GPIO.setup(pin, GPIO.OUT)



######################
#    GPIO FUNCTIONS  #
######################

def blink_all():
    """Turn all pins on, sleep, turn all pins off"""

    
    any(on(pin) for pin in pin_numbers)
    time.sleep(0.5)
    any(off(pin) for pin in pin_numbers)
    time.sleep(0.5)


def all_pins_off():
    """Turn off all pins"""
    any(off(pin) for pin in pin_numbers)


def getInterval(song):
    bpm = get_file_bpm(song)
    interval = 1/(bpm/60)

    return interval
