from luma.core.interface.serial import i2c, spi, pcf8574
from luma.core.interface.parallel import bitbang_6800
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1309, ssd1325, ssd1331, sh1106, ws0010


def init():
    serial = spi(device=0, port=0)
    print(serial)
    device = sh1106(serial)
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((30, 30), "IP: ", fill="white")
        draw.text((30, 40), "Hello World", fill="white")