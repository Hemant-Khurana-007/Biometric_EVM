from machine import UART,Pin
import time
import sys
from pf import PyFingerprint
from machine import PWM

servo1 = PWM(Pin(18), freq=50)
servo2 = PWM(Pin(21), freq=50)
e={1:"no",2:"no",3:"no",4:"no",5:"no",6:"no"}
d={1:"siwan",2:"matihani",3:"newdelhi",4:"rajourigarden",5:"siwan",6:"newdelhi"}

def set_angle1(angle):
    duty = int(40 + (angle / 180) * 75)
    servo1.duty(duty)

def set_angle2(angle):
    duty2 = int(40 + (angle / 180) * 75)
    servo2.duty(duty2)

esp_b = UART(1, baudrate=115200, tx=4, rx=5)
uart = UART(2, baudrate=57600, tx=17, rx=16)
sensor = PyFingerprint(uart)
mosfet = Pin(25, Pin.OUT)

esp_b.write("connection established"+"\n")

def read_from_pi(timeout_ms=1000):
    start = time.ticks_ms()
    while time.ticks_diff(time.ticks_ms(), start) < timeout_ms:
        try:
            line = sys.stdin.readline()
            if line:
                return line.strip().lower()
        except:
            pass
        time.sleep(0.05)
    return None

def mark():          
    set_angle1(0)
    mosfet.on()
    time.sleep(0.014)
    mosfet.off()
    time.sleep(1)
    set_angle2(0)
    time.sleep(1)
    set_angle2(130)
    time.sleep(1)
    set_angle1(180)
    time.sleep(1)

def enroll_finger(slot):
    while not sensor.readImage():
        pass
    try:
        sensor.convertImage(1)
    except:
        sys.stdout.write("invalid input")
        enroll_finger(slot)
    else:
        while not sensor.readImage():
            pass
        try:
            sensor.convertImage(2)
        except:
            sys.stdout.write("invalid input")
            enroll_finger(slot)
        else:
            sensor.createTemplate()
            sensor.storeTemplate(slot)
enroll_finger(6)
while True:
    time.sleep(1)
    if sensor.readImage():
        try:
            sensor.convertImage(1)
        except:
            sys.stdout.write("invalid input")
        try:
            result = sensor.searchTemplate()
            position = result[0]
            if position >= 0:
                
                if e[position]=="no":
                    mark()
                    esp_b.write(d[position] + "\n")
                    e[position]="yes"
                    sys.stdout.write("{}\n".format(d[position]))
            else:
                sys.stdout.write("No match found.")
        except:
            while True:
                if sensor.readImage():
                    pass
                else:
                    break
                time.sleep(0.5)
        



