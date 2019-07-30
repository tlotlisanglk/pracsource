from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
c = 0

def button_callbackup(channel):
	global c
	c = (c + 1) % 8
	GPIO.output(18, (c >> 0) & 1)
	GPIO.output(22, (c >> 1) & 1)
	GPIO.output(11, (c >> 2) & 1)
	print(c)
def button_callbackdown(channel):
	global c
	c = (c - 1) % 8
	GPIO.output(18, (c >> 0) & 1)
	GPIO.output(22, (c >> 1) & 1)
	GPIO.output(11, (c >> 2) & 1)
	print(c)

GPIO.add_event_detect(16,GPIO.RISING,callback=button_callbackup,bouncetime=200)
GPIO.add_event_detect(12,GPIO.RISING,callback=button_callbackdown,bouncetime=200)

while True:
	sleep(.1)





