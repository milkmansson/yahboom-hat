import smbus
import time
import os
import sys
from datetime import datetime
from array import *

def setfanspeed(oVal):
    try:
        bus.write_byte_data(addr, fan_reg, oVal)
    except:
        exc_tuple = sys.exc_info()
        print("setfanspeed [0]:" + exc_tuple[0] + " [1]:" + exc_tuple[1] + " [2]:" + exc_tuple[2])

def setRGBEffect(effect):
    try:
        if effect >= 0 and effect <= 4:
            bus.write_byte_data(addr, rgb_effect_reg, effect&0xff)
    except:
        exc_tuple = sys.exc_info()
        print("setRGBEffect [0]:" + exc_tuple[0] + " [1]:" + exc_tuple[1] + " [2]:" + exc_tuple[2])

def setRGBSpeed(speed):
    try:
        if speed >= 1 and speed <= 3:
            bus.write_byte_data(addr, rgb_speed_reg, speed&0xff)
    except:
        exc_tuple = sys.exc_info()
        print("setRGBSpeed [0]:" + exc_tuple[0] + " [1]:" + exc_tuple[1] + " [2]:" + exc_tuple[2])

def setRGBColor(color):
    try:
        if color >= 0 and color <= 6:
            bus.write_byte_data(addr, rgb_color_reg, color&0xff)
    except:
        exc_tuple = sys.exc_info()
        print("setRGBColor [0]:" + exc_tuple[0] + " [1]:" + exc_tuple[1] + " [2]:" + exc_tuple[2])

def setrgb(num,r,g,b):
    try:
        #turn lights off first
        #bus.write_byte_data(addr, rgb_off_reg, 0x00)
        if num >= max_led:
            bus.write_byte_data(addr,0x00,0xff)
            bus.write_byte_data(addr,0x01,r&0xff)
            bus.write_byte_data(addr,0x02,g&0xff)
            bus.write_byte_data(addr,0x03,b&0xff)
        elif num >= 0:
            bus.write_byte_data(addr,0x00,num&0xff)
            bus.write_byte_data(addr,0x01,r&0xff)
            bus.write_byte_data(addr,0x02,g&0xff)
            bus.write_byte_data(addr,0x03,b&0xff)
    except:
        exc_tuple = sys.exc_info()
        print("setrgb [0]:" + exc_tuple[0] + " [1]:" + exc_tuple[1] + " [2]:" + exc_tuple[2])


bus = smbus.SMBus(1)
addr = 0x0d
fan_reg = 0x08
state = 0
temp = 0
level_temp = 0
rgb_effect_reg = 0x04
rgb_speed_reg = 0x05
rgb_color_reg = 0x06
rgb_off_reg = 0x07
max_led = 3
rgb = [0x00, 0x00, 0x00, 0x00]

bus.write_byte_data(addr, rgb_off_reg, 0x00)
time.sleep(1)
setRGBEffect(1)
setRGBSpeed(3)
setRGBColor(4)


while True:
    cmd = os.popen('vcgencmd measure_temp').readline()
    CPU_TEMP = cmd.replace("temp=","").replace("'C\n","")
    temp = float(CPU_TEMP)

    if abs(temp - level_temp) >= 1:
        if temp <= 40:
            level_temp = 40
            fan_speed = 0x7
            rgb = [max_led, 0x00, 0x00, 0xff]
        elif temp <= 45:
            level_temp = 0x7
            fan_speed = 0x7
            rgb = [max_led, 0x1e, 0x90, 0xff]
        elif temp <= 47:
            level_temp = 47
            fan_speed = 0x08
            rgb = [max_led, 0x00, 0xbf, 0xff]
        elif temp <= 49:
            level_temp = 49
            fan_speed = 0x06
            rgb = [max_led, 0x5f, 0x9e, 0xa0]
        elif temp <= 51:
            level_temp = 51
            fan_speed = 0x09
            rgb = [max_led, 0xff, 0xff, 0x00]
        elif temp > 51:
            level_temp = 52
            fan_speed = 0x01
            rgb = [max_led, 0xff, 0x00, 0x00]
        else:
            level_temp = 0
            fan_speed = 0x01
            rgb = [max_led, 0xff, 0xff, 0xff]
            print('Something wrong: choosing fan reg 0x01 instead')
    setfanspeed(fan_speed)
    print(CPU_TEMP + 'c: <' + str(level_temp) + ' : choosing fan reg ' + str(hex(fan_speed)))
    setrgb(rgb[0],rgb[1],rgb[2],rgb[3])
    sys.stdout.flush()
    time.sleep(4)
    
