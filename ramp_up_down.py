"""
Ramp up motors' speed forward in 4 seconds. 
Slow down motors' speed forward in 4 seconds. 
Ramp up motors' speed backward in 4 seconds. 
Slow down motors' speed backward in 4 seconds. 
Stop motors.
"""

from machine import Pin, PWM
from time import sleep

# SETUP

# Config Pins
INA_LEFT = Pin(20, Pin.OUT)  # 3
INB_LEFT = Pin(21, Pin.OUT)   # 4
INA_RIGHT = Pin(12, Pin.OUT)  # 8, 9->12 on paper 
INB_RIGHT = Pin(11, Pin.OUT)  # 9  8->12 on paper 
INA_LEFT.off()
INB_LEFT.off()
INA_RIGHT.off()
INB_RIGHT.off()
PWM_LEFT = PWM(Pin(19))  # 2
PWM_RIGHT = PWM(Pin(10))  # 7
PWM_LEFT.freq(1000)
PWM_RIGHT.freq(1000)

ramp_time = 4
ramp_step = 100
no_steps = int(ramp_time * 1000 / ramp_step)  # convert to milliseconds

def stop():
    PWM_LEFT.duty_u16(0)   
    INA_LEFT.off()
    INB_LEFT.off()
    PWM_RIGHT.duty_u16(0)
    INA_RIGHT.off()
    INB_RIGHT.off()

def ramp_forward_up():
    INB_LEFT.on()
    INB_RIGHT.on()
    for duty in range(0, 65025, int(65025 / no_steps)):
        PWM_LEFT.duty_u16(duty)
        PWM_RIGHT.duty_u16(duty)
        sleep(ramp_step / 1000)  # sleep for ramp_step in seconds
    sleep(1)  # pause at full speed
    stop()

def ramp_forward_down():
    INB_LEFT.on()
    INB_RIGHT.on()
    for duty in range(65025, 0, -int(65025 / no_steps)):
        PWM_LEFT.duty_u16(duty)
        PWM_RIGHT.duty_u16(duty)
        sleep(ramp_step / 1000)  # sleep for ramp_step in seconds
    stop()

def ramp_backward_up():
    INA_LEFT.on()
    INA_RIGHT.on()
    for duty in range(0, 65025, int(65025 / no_steps)):
        PWM_LEFT.duty_u16(duty)
        PWM_RIGHT.duty_u16(duty)
        sleep(ramp_step / 1000)  # sleep for ramp_step in seconds
    sleep(1)  # pause at full speed
    stop()

def ramp_backward_down():
    INA_LEFT.on()
    INA_RIGHT.on()
    for duty in range(65025, 0, -int(65025 / no_steps)):
        PWM_LEFT.duty_u16(duty)
        PWM_RIGHT.duty_u16(duty)
        sleep(ramp_step / 1000)  # sleep for ramp_step in seconds
    stop()

# LOOP
ramp_forward_up()
sleep(0.1)  # Wait before next action
ramp_forward_down()
sleep(0.1)  # Wait before next action
ramp_backward_up()
sleep(0.1)  # Wait before next action
ramp_backward_down()
stop()
