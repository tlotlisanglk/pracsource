from time import sleep	# get sleep funtion from time class
import RPi.GPIO as GPIO # get GPIO from RPi library

print("Count up using left button and down using right button:\n") # User guide message
GPIO.setwarnings(False) # remove warnings of pins
GPIO.setmode(GPIO.BOARD) # set the mode of board to use pin numbers
GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_UP) # set the pin number for input
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP) # set the pin number for input
GPIO.setup(11,GPIO.OUT)	# set pin 11 as the output
GPIO.setup(18,GPIO.OUT) # set pin 18 as the output
GPIO.setup(22,GPIO.OUT) # set pin 22 as the output
c = 0 # declare global variable

def button_callbackup(channel):	# define the upcounter funtion
	global c		# use the global variable c
	c = (c + 1) % 8		# increament c and find its remainder value
	GPIO.output(18, (c >> 0) & 1) # is the 0 bit of value c set
	GPIO.output(22, (c >> 1) & 1) # is the 1 bit of value c set
	GPIO.output(11, (c >> 2) & 1) # is the 2 bit of value c set
	print(c)		      # Testing if value of c is incrementing	
def button_callbackdown(channel): # define the downcounter function
	global c		  # define global variable c
	c = (c - 1) % 8 # decrement c and find its remainder vulue
	GPIO.output(18, (c >> 0) & 1)  # is the 0 bit of value c set
	GPIO.output(22, (c >> 1) & 1)  # is the 0 bit of value c set
	GPIO.output(11, (c >> 2) & 1)  # is the 0 bit of value c set
	print(c)		       # Test if the value of c is decrementing

GPIO.add_event_detect(16,GPIO.RISING,callback=button_callbackup,bouncetime=200) # an interrupt for counting down funtion
GPIO.add_event_detect(12,GPIO.RISING,callback=button_callbackdown,bouncetime=200) # an interrupt for counting up function

while True:
	sleep(.1)






