from datetime import datetime
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219
from PIL import ImageFont

class Menu():
    def __init__(self, device):
        self.virtual = viewport(device.device, width=32, height=8)
        self.fnt = device.fnt

    def render(self, draw): 
        draw.text((3,-2), "MENU", font=self.fnt, fill="white")
