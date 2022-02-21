import RPi.GPIO as GPIO  
from raspberrydisplay.display import Display
from gpiozero import Button
import time
import configparser

def use_display(display_time):
    display = Display()
    for i in range (display_time):
            display.refresh()
            time.sleep(1)
    display.turn_off()
    print("Display is off")

def run():
    # getting app config
    config = configparser.ConfigParser()
    config.read('config.ini')
    display_time = int(config['DISPLAY']['display_time'])

    GPIO.setmode(GPIO.BCM)  
  
    # GPIO 23 set up as input. It is pulled up to stop false signals  
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

    while 1:
        try:  
            time.sleep(1)
            GPIO.wait_for_edge(23, GPIO.FALLING)  
            use_display(display_time)
        except KeyboardInterrupt:  
            print("exiting...")
            GPIO.cleanup()       # clean up GPIO on CTRL+C exit 
            break
            
            
    GPIO.cleanup()           # clean up GPIO on normal exit  


