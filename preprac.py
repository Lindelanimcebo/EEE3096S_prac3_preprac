import RPi.GPIO as GPIO
import time

# Set up
GPIO.setmode(GPIO.BOARD)

LED = 16 
SWITCH = 18

GPIO.setup(SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED,GPIO.OUT)

def toggle(pin):
	GPIO.output(LED, not GPIO.input(LED))

def main():
	GPIO.add_event_detect(SWITCH, GPIO.FALLING, callback=toggle, bouncetime = 200)
	while True:
		time.sleep(0.01)

if __name__ == "__main__":
	# Making sure that GPIO stopped correctly
	try:
		main()
	except KeyboardInterrupt:
		print("Exiting Nicely!")
	except Exception as e:
		print("Some other error occured: {}".format(e.message))
	finally:
		GPIO.cleanup()




