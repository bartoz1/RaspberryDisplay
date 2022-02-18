from luma.core.interface.serial import i2c, spi, pcf8574
from luma.core.interface.parallel import bitbang_6800
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1309, ssd1325, ssd1331, sh1106, ws0010
import socket
import urllib.error
import urllib.request
from raspberrydisplay.db import DB
import configparser
from gpiozero import CPUTemperature, LoadAverage


import RPi.GPIO as GPIO
GPIO.setwarnings(False)
    
LOADING_TEXT = 'loading...'


class Display:
    def __init__(self):
        self._config = configparser.ConfigParser()
        self._config.read('config.ini')

        self.ip = LOADING_TEXT
        self.db_status = LOADING_TEXT
        self._serial = spi(device=0, port=0)
        
        self._device = sh1106(self._serial)

        # connect DB only if allowed in config.ini
        if self._config['mysqlDB']['check_db'] == 'True':
            self._db = DB()
        else:
            self._db = None
            self.db_status = 'MySQL disabled'
        
        self.refresh()

    # check internet, db (if enabled), and refresh desplay
    def refresh(self):
        self._check_internet()
        if self._db is not None:
            self.db_status = self._db.get_last_update()
        cpu = CPUTemperature()
        cpu_temp = round(cpu.temperature)
        cpu_usage = str(int(LoadAverage(minutes=1).load_average*100))

        # Displaying all the info
        with canvas(self._device) as draw:
            draw.rectangle(self._device.bounding_box, outline="white", fill="black")
            draw.text((5, 20), f'CPU usage: {cpu_usage}%', fill="white")
            draw.text((5, 30), f'CPU: {cpu_temp}\u00B0C', fill="white")
            draw.text((5, 40), f'IP: {self.ip}', fill="white")
            draw.text((5, 50), f'{self.db_status}', fill="white")
            
            print('all')

    def turn_off(self):
        self._device.command(0xAE)  # display off signal

    def _internet_on(self):
        try:
            urllib.request.urlopen('http://www.wp.pl', timeout=1)
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
