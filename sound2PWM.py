import machine
import time

sound = machine.ADC(26)

led = machine.Pin(15, machine.Pin.OUT)
led = machine.PWM(led)
led.duty_u16(0)

while True:
    amp = sound.read_u16()
    amp -= 15000
    amp = abs(amp)
    amp*=10
    print(amp)
    led.duty_u16(amp)
    time.sleep(0.1)
