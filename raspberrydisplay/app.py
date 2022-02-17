from raspberrydisplay.internet_connection import check_internet
from raspberrydisplay.display import Display
from gpiozero import Button
import time

button = Button(23)

def run():
    check_internet()
    display = Display()
    while True:
        #button.wait_for_press()
        #print("Button pressed!")
        check_internet()
        
        display.refresh()
        time.sleep(5)
        #time.sleep(30)