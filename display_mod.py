from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219
from PIL import ImageFont

from datetime import datetime

class Display():
    def __init__(self):
        self.contrast = 0
        self.serial = spi(port=0, device=0, gpio=noop())
        self.device = max7219(self.serial, cascaded=4, block_orientation=-90)
        self.device.contrast(self.contrast)

        self.fnt = ImageFont.truetype("fonts/slkscr.ttf", 8)

    def clear(self):
        self.device.clear()

    def draw(self, view):
        with canvas(view.virtual) as draw:
            view.render(draw)
