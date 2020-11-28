import RPi.GPIO as GPIO
import time
import datetime
import os
import sys
from led import led_functions


import requests

def sendimage(imagename):
    url = "https://api.telegram.org/bot1419399111:AAHypXWv5iyeobNJAm8gwtHDHlCTx6LHFfY/sendPhoto"
    print(imagename)
    image=f"/home/pi/Desktop/images/{imagename}.jpg"
    files = {'photo': open(image, 'rb')}
    data = {'chat_id': "35854268"}
    r = requests.post(url, files=files, data=data)
    print(r.status_code, r.reason, r.content)
    url2 = f"https://api.telegram.org/bot1419399111:AAHypXWv5iyeobNJAm8gwtHDHlCTx6LHFfY/sendMessage?chat_id=35854268&text= a movment detected at - {imagename}"
    r2 = requests.post(url2)


#

GPIO.setmode(GPIO.BOARD)
PIR_PIN = 26
GPIO.setup(PIR_PIN, GPIO.IN)

try:
               time.sleep(2)
               print ("Ready")
               while True:
                             if GPIO.input(PIR_PIN):
                              print ("Motion Detected!")
                              strtime=datetime.datetime.now().strftime("%Y-%m-%d---%H:%M:%S")
                              os.system(f'fswebcam -r 1280x720 -S 3 --jpeg 50 --save /home/pi/Desktop/images/{strtime}.jpg')
                              sendimage(strtime)
                              led_functions.led_action('red', 2, 0.1)
                              time.sleep(5)
except KeyboardInterrupt:
               print ("Quit")
               GPIO.cleanup()
