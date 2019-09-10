import time
import datetime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
TopLeft = 37
BottomLeft = 35
TopRight = 33
BottomRight = 31
Servo = 40
GPIO.setup(TopLeft, GPIO.OUT)
GPIO.setup(TopRight, GPIO.OUT)
GPIO.setup(BottomLeft, GPIO.OUT)
GPIO.setup(BottomRight, GPIO.OUT)
GPIO.setup(Servo, GPIO.OUT)

p = GPIO.PWM(Servo, 50)
p.start(5)
x = input()
x = x/10 + 2.5

p.ChangeDutyCycle(x)
time.sleep(0.5)


