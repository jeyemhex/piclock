from datetime import datetime
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219
from PIL import ImageFont

class Clock():
    max_bar_width = 30
    seconds_in_a_day = 86400
    num_modes = 3
    def __init__(self, device):
        self.virtual = viewport(device.device, width=32, height=8)
        self.fnt = device.fnt
        self.mode = 0

    def render(self, draw): 
        now = datetime.now()

        if self.mode == 0: # Time
            current_time = now.strftime("%H:%M")

            bar_width = int(self.max_bar_width * now.second / 60)

            draw.line([(1,7), (1+bar_width,7)] , fill="white")
            draw.text((3,-2), current_time, font=self.fnt, fill="white")
            if not now.second % 2:
                draw.text((14,-2), ":", font=self.fnt, fill="black")

        elif self.mode == 1: # Date
            current_date = now.strftime("%d/%m")

            bar_width = self.max_bar_width * (now.hour*60*60 + now.minute*60 + now.second) / self.seconds_in_a_day 
            draw.line([(1,7), (1+bar_width,7)] , fill="white")
            draw.text((3,-2), current_date, font=self.fnt, fill="white")

        elif self.mode == 2: # Weather
            current_climate = now.strftime("19°C")

            bar_width = self.max_bar_width * 0.4
            draw.line([(1,7), (1+bar_width,7)] , fill="white")
            draw.text((3,-2), current_climate, font=self.fnt, fill="white")
