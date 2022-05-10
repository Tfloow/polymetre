import time
from dht11 import DHT11
import machine

IR = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)
GAS = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_UP)
led = machine.Pin(15, machine.Pin.OUT)
led = machine.PWM(led)
servo = machine.PWM(machine.Pin(7))
sound = machine.ADC(27)

servo.freq(50)
servo.duty_u16(1638)
led.duty_u16(0)
timing = 60

def servoSecure(pourcentage):
    if pourcentage >1:
        return 8192
    valueServo = [1638, 8192]
    #return int(valueServo[0]+pourcentage*valueServo[-1]) for the sake of the servo
    return 1638
    


def readTaHData():
    DATA = dht.read_data()    
    t = DATA[0]
    h = DATA[1]                                                    
    return [str(t),str(h)]

def read_Data(self):
    global dat
    global code_dis_flag
    if IR.value() == 1:
        lol = 0
    else:
        cnt = 0
        while IR.value()==0 and cnt < 400:
            time.sleep_us(7)
            cnt +=1
            continue
        if cnt >= 400 or cnt < 230:
            lol = 0
        else:
            if IR.value()==1:
                cnt = 0
                while IR.value()==1 and cnt < 215:
                    time.sleep_us(7)
                    cnt +=1
                    continue
                if cnt >= 215 or cnt < 100:
                    lol = 0
                else:
                    data=[]
                    j=0
                    while j<32:
                        cnt = 0    
                        while IR.value()==0 and cnt < 30:
                            time.sleep_us(7)
                            cnt +=1
                            continue
                        if cnt >= 30 or cnt < 10:
                            print('CL_bit',j)
                        else:
                            cnt = 0 
                            while IR.value()==1 and cnt < 70:
                                time.sleep_us(7)
                                cnt +=1
                                continue
                            if cnt >= 70 or cnt < 10:
                                print('CH_bit',j)
                            else:
                                if cnt > 35:
                                    data.append(1)
                                else:
                                    data.append(0)
                        j+=1            
                    
                    code3 = data[16:24]
                    code4 = data[24:32]
                    code3_buf = 0
                    code4_buf = 0
                    for i in range(8):
                        code3_buf+=code3[i]*2**(7-i)
                        code4_buf+=code4[i]*2**(7-i)
                    if code3_buf+code4_buf == 255:
                        dat = code3_buf
                        print('IR code:',dat)                       
                        code_dis_flag = 1

IR.irq(handler=read_Data, trigger=machine.Pin.IRQ_FALLING)                     #IO Interrupts
dat = 0
code_dis_flag = 0
old = 0

while True:    
    if dat == 162:
        old = 162
        dht = DHT11(3) 
        res = readTaHData()
        temp = int(res[0])
        if temp > 40:
            break
        led.duty_u16(int(65534*temp/40))
        servo.duty_u16(servoSecure(temp/40))
        print(temp, type(temp))
        time.sleep(0.5)
    if dat == 98:
        old = 98
        dht = DHT11(3) 
        res = readTaHData()
        hum = int(res[1])
        led.duty_u16(int(65534*hum/100))
        servo.duty_u16(servoSecure(hum/100))
        time.sleep(0.5)
        print(hum)
    if dat == 176:
        old = 176
        time.sleep(30/timing)
        led.duty_u16(65534)
        servo.duty_u16(1638)
        time.sleep(30/timing)
        led.duty_u16(0)
        servo.duty_u16(3276*2)
    if dat == 24:
        timing += 10
        print("incremented")
        dat = old
    if dat == 74:
        if timing >10:
            timing-= 10
            print("lowered")
        else:
            print("could not go lower")
        dat = old
    if dat == 226:
        old = 226
        if GAS.value():
            led.duty_u16(0)
            servo.duty_u16(1638)
            print("no problem")
            time.sleep(1)
        else:
            led.duty_u16(3000)
            servo.duty_u16(8192)
            time.sleep(1)
    if dat == 34:
        old = 34
        print(sound.read_u16())
        led.duty_u16(sound.read_u16())
        servo.duty_u16(servoSecure(sound.read_u16()/65534))
        time.sleep(0.1)
    if dat == 104:
        led.duty_u16(0)
        servo.duty_u16(1638)
    if dat == 152:
        break
