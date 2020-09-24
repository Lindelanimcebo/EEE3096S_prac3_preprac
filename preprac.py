import RPi.GPIO as GPIO
import time

# Set up
GPIO.setmode(GPIO.BOARD)

LED = 16 
SWITCH = 18

GPIO.setup(SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED,GPIO.OUT)

def main():
	time.sleep(0.5)
	GPIO.output( LED, not GPIO.input(LED) )

if __name__ == "__main__":
	# Making sure that GPIO stopped correctly
	try:
		while True:
			main()
	except KeyboardInterrupt:
		print("Exiting Nicely!")
		GPIO.cleanup()
	except e:
		print("Some other error occured: {}".format(e.message))
		GPIO.cleanup()





