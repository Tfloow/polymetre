import machine
import time

led = machine.Pin(15, machine.Pin.OUT)
seqStart = machine.Pin(14, machine.Pin.OUT)
clockLed = machine.Pin(13, machine.Pin.OUT)

max = 64000
place = 64
value = 49500
div = 1000000000
print(200/div)
seqStart.value(1)

def clock(div, Clkpin, Cspin, Dinpin, binary):
    flag = 0
    duty = 80
    drap = 0
    
    Cspin.value(0)
    
    for f in range(16):
        if not flag:
            time.sleep(30/div)
            Dinpin.value(int(binary[f]))
            print(binary[f])
            time.sleep(50/div)
            if not drap:
                drap = 1
            else:
                drap = 0
            Clkpin.value(drap)
            
    Cspin.value(1)
    time.sleep(duty/div)


toConvert = int(place*value/max)
print(toConvert)
print(bin(toConvert))
signal = str(0)*16
signal = list(signal)
index = 0
result = str(bin(toConvert)).strip("0b")
for f in range(len(result)-1,-1,-1):
    signal[15-index] = result[f]
    index += 1
print(signal)
"""
seqStart.value(0)
for f in signal:
    led.value(int(f))
    time.sleep(1)
seqStart.value(1)
    
led.value(0)
time.sleep(0.5)"""


def testing():
    time.sleep(0.8)
    clock(div, clockLed, seqStart, led, signal)
    clockLed.value(0)
    led.value(0)
    seqStart.value(0)
    
for f in range(50):
    testing()
