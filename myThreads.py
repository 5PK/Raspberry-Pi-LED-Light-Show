
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

import threading


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)



class blinkThread(threading.Thread):
    def __init__(self):
        self._kill = threading.Event()
        self.on = lambda pin: GPIO.output(pin, 1)
        self.off = lambda pin: GPIO.output(pin, 0)
        self.pins = [7, 1, 8]

        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)

        super(blinkThread, self).__init__() 

    def run(self):
        
        while not self._kill.is_set():
            print('here' )
            self.blink_all()
    def kill(self):
        self._kill.set()

    
    def blink_all(self):
        """Turn all pins on, sleep, turn all pins off"""
            
        any(self.on(pin) for pin in self.pins)
        time.sleep(0.5)
        any(self.off(pin) for pin in self.pins)
        time.sleep(0.5)


class playMusicThread(threading.Thread):
    def __init__(self, song):
        self._kill = threading.Event()

        self.CHUNK = 1024

        self.wf = wave.open(song)

        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(
                        format=self.p.get_format_from_width(self.wf.getsampwidth()),
                        channels=self.wf.getnchannels(),
                        rate=self.wf.getframerate(),
                        output=True
                        )

        self.data = self.wf.readframes(self.CHUNK)
 
        super(playMusicThread, self).__init__() 

    def run(self):
        
        while len(self.data) > 0:
            while not self._kill.is_set():
                self.stream.write(self.data)
                self.data = self.wf.readframes(self.CHUNK)

        self.stream.stop_stream()
        self.stream.close()

        self.p.terminate()

    def kill(self):
        self._kill.set()



class playLightThread(threading.Thread):
    def __init__(self, interval):
        self._kill = threading.Event()
       
        self.interval = interval

        self.on = lambda pin: GPIO.output(pin, 1)
        self.off = lambda pin: GPIO.output(pin, 0)
        
        self.pins = [7, 1, 8]
        self.RED = 7
        self.GREEN = 1
        self.BLUE = 8

        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)

        super(playLightThread, self).__init__() 

    def run(self):
        
        while not self._kill.is_set():
            
  
    
            self.playLights(self.interval)
    
    
    
    def kill(self):
        self._kill.set()



    def playLights(self, interval):

        light = random.randrange(1, 8)
        
        self.chooseLightOn(light)
        time.sleep(interval)
        self.chooseLightOff(light)
        time.sleep(interval)

    def chooseLightOn(self, light):
    
        # RED
        if light == 1:
            self.on(self.RED)
        elif light == 2:
            self.on(self.GREEN)
        elif light == 3:
            self.on(self.BLUE)
        elif light == 4:
            self.on(self.RED)
            self.on(self.GREEN)
        elif light == 5:
            self.on(self.RED)
            self.on(self.BLUE)
        elif light == 6:
            self.on(self.GREEN)
            self.on(self.BLUE)
        elif light == 7:
            self.on(self.RED)
            self.on(self.BLUE)
            self.on(self.GREEN)


    def chooseLightOff(self, light):
    
        # RED
        if light == 1:
            self.off(self.RED)
        elif light == 2:
            self.off(self.GREEN)
        elif light == 3:
            self.off(self.BLUE)
        elif light == 4:
            self.off(self.RED)
            self.off(self.GREEN)
        elif light == 5:
            self.off(self.RED)
            self.off(self.BLUE)
        elif light == 6:
            self.off(self.GREEN)
            self.off(self.BLUE)
        elif light == 7:
            self.off(self.RED)
            self.off(self.BLUE)
            self.off(self.GREEN)



    
             

