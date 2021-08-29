from luma.core.interface.serial import i2c, spi, pcf8574
from luma.core.interface.parallel import bitbang_6800
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1309, ssd1325, ssd1331, sh1106, ws0010
import socket
import urllib.error
import urllib.request
from raspberrydisplay.db import DB

import RPi.GPIO as GPIO
GPIO.setwarnings(False)

IP_ADRESS = 'loading...'
class Display:
    def __init__(self):
        self.ip = 'loading...'
        self.updt = 'loading...'
        self._serial = spi(device=0, port=0)
        #print(serial)
        self._device = sh1106(self._serial)
        #print(device)
        self._db = DB()
        
        self.refresh()
            
    def refresh(self):
        self._check_internet()
        self.updt = self._db.get_last_update()
        with canvas(self._device) as draw:
            draw.rectangle(self._device.bounding_box, outline="white", fill="black")
            draw.text((5, 40), f'IP: {self.ip}', fill="white")
            draw.text((5, 50), f'{self.updt}', fill="white")
            print('all')



    def _internet_on(self):
        try:
            urllib.request.urlopen('http://www.google.com', timeout=1)
            return True
        except urllib.error.URLError as err:
            return False


    def _get_local_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        return ip


    def _check_internet(self):
        if self._internet_on():
            ip = self._get_local_ip()
            self.ip = ip
        else:
            self.ip = 'not available'
