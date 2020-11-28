import RPi.GPIO as GPIO
import time
import random




def led_action(color_picker,time_in,interval):

    colors = {'blue': '40', 'green': '38', 'red': '36', 'yellow': '38,36', 'purple': '36,40', 'cyan': '40,38',
              'white': '36,38,40'}
    if color_picker in colors:
        pins=colors[color_picker]

    else:
        return False

    if len(pins)==5:
        cnt=2
    elif len(pins)==8:
        cnt=3
    else:
        cnt=1

    my_aaray=[]
    my_aaray=pins.split(',',cnt)




    for times in range(time_in):
        if cnt==1:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            GPIO.setup(int(my_aaray[0]), GPIO.OUT)
            GPIO.output(int(my_aaray[0]), GPIO.HIGH)
            time.sleep(interval)
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            GPIO.setup(int(my_aaray[0]), GPIO.OUT)
            GPIO.output(int(my_aaray[0]), GPIO.LOW)
            time.sleep(interval)
        if cnt==2:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            GPIO.setup(int(my_aaray[0]), GPIO.OUT)
            GPIO.setup(int(my_aaray[1]), GPIO.OUT)
            GPIO.output(int(my_aaray[0]), GPIO.HIGH)
            GPIO.output(int(my_aaray[1]), GPIO.HIGH)
            time.sleep(interval)
            GPIO.output(int(my_aaray[0]), GPIO.LOW)
            GPIO.output(int(my_aaray[1]), GPIO.LOW)
            time.sleep(interval)
        if cnt==3:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            GPIO.setup(int(my_aaray[0]), GPIO.OUT)
            GPIO.setup(int(my_aaray[1]), GPIO.OUT)
            GPIO.setup(int(my_aaray[2]), GPIO.OUT)
            GPIO.output(int(my_aaray[0]), GPIO.HIGH)
            GPIO.output(int(my_aaray[1]), GPIO.HIGH)
            GPIO.output(int(my_aaray[2]), GPIO.HIGH)
            time.sleep(interval)
            GPIO.output(int(my_aaray[0]), GPIO.LOW)
            GPIO.output(int(my_aaray[1]), GPIO.LOW)
            GPIO.output(int(my_aaray[2]), GPIO.LOW)
            time.sleep(interval)


    return True








