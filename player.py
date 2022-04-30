from notation import sheet
from tone import TONE

from gpiozero import PWMOutputDevice
import time

PIN = 12

def init():
    global bz
    bz = PWMOutputDevice(PIN, True, 0.5)

def beep(freq, duration):
    bz.frequency = freq
    time.sleep(duration)

def play():
    for s in sheet:
        beep(TONE[s[0]] if s[0] in TONE else 1, s[1])

if __name__ == "__main__":
    init()
    play()
