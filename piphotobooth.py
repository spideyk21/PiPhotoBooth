#!/usr/bin/env python3
#title           : piphotobooth.py
#description     : Raspberry Pi based Photo Booth
#author          : spideyk21
#date            : MM/DD/YYYY
#version         : X.X
#usage           : 
#refrence        : http://www.drumminhands.com/2014/06/15/raspberry-pi-photo-booth/
#				   http://www.raspberrypi.org/documentation/usage/camera/python/README.md
#				   http://picamera.readthedocs.io/
#				   https://www.raspberrypi.org/documentation/raspbian/applications/camera.md
#
#python_version  : 3.0 (sudo apt-get install python3-picamera)
#notes			 : written using gpiozero (https://gpiozero.readthedocs.org/)
#==============================================================================

# Import required Python libraries
from gpiozero import LED, Button
import picamera
from datetime import datetime
import time
import os

#Buttons
button_takepic = Button(#) #capture mode: picture/video (true=picture, false=video)

#LED's
led_active = LED(#) #Flashs when picture is taken or video is being recorded.
led_pwr = LED(#) # power light

camera = picamera.PiCamera

date = time.strftime("%Y%m%d_%H%M%S")
pic_loc = "/home/pi/trailcam/pictures/"


def take_picture():
	#os.system ("raspistill -n -vf -hf -o " + pic_loc + DATE + ".jpg") #sh command
	camera.capture('image.jpg')

	
while True:
	if button_takepic.is_pressed
		print("Taking Picture")
		print("Get Ready") #countdown
		take_picture
		
		