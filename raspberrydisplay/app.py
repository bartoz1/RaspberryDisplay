from raspberrydisplay.internet_connection import check_internet
from raspberrydisplay.display import Display
import time

def run():
    display = Display()
    while True:
        check_internet()
        display.refresh()
        time.sleep(30)