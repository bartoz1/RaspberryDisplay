from raspberrydisplay.internet_connection import check_internet
from raspberrydisplay.display import Display
from gpiozero import Button
import time

button = Button(23)

def run():
    check_internet()
    display = Display()
    while True:
        button.wait_for_press()
        print("kliknieto przycisk!")
        check_internet()
        
        display.refresh()
        time.sleep(30)
        #time.sleep(30)