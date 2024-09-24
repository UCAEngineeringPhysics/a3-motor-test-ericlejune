"""
Spin motors for 1 minute at 50% duty cycle
"""
from machine import Pin, PWM
from time import sleep

# SETUP

# Config Pins
INA_LEFT = Pin(20, Pin.OUT) #3
INB_LEFT = Pin(21, Pin.OUT) #4
INA_RIGHT = Pin(12, Pin.OUT) #8, 9->12 on paper but flipped bc motor is flipped
INB_RIGHT = Pin(11, Pin.OUT) #9  8->12 on paper but flipped bc motor is flipped
INA_LEFT.off()
INB_LEFT.off()
INA_RIGHT.off()
INB_RIGHT.off()
PWM_LEFT = PWM(Pin(19)) #2
PWM_RIGHT = PWM(Pin(10)) #7
PWM_LEFT.freq(1000)
PWM_RIGHT.freq(1000)

#STOP
def stop():
    PWM_LEFT.duty_u16(0)   
    INA_LEFT.off()
    INB_LEFT.off()
    PWM_RIGHT.duty_u16(0)
    INA_RIGHT.off()
    INB_RIGHT.off()
    
#forward
def forward():
    INB_LEFT.on()
    PWM_LEFT.duty_u16(int(65025/2))
    INB_RIGHT.on()
    PWM_RIGHT.duty_u16(int(65025/2))
    sleep(60)
    stop()
# LOOP
forward()
#120 wheel 1
#125 wheel 2 
