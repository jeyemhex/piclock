import enum
import time
from pyky040 import pyky040
import threading

from display_mod import Display
from clock_mod import Clock
from menu_mod import Menu

class Mode(enum.Enum):
    CLOCK = 1
    MENU = 2


mode = Mode.CLOCK
display = Display()
views = {
  "clock": Clock(display),
  "menu": Menu(display),
}

encoder = {
  "time": time.time(), 
  "threshold": 0.3,
}

def encoder_inc(dummy):
    global views, encoder, mode
    cur_time = time.time()
    if (cur_time - encoder["time"]) > encoder["threshold"]:
        print("Incrementing encoder")
        encoder["time"] = time.time()
        if mode == Mode.CLOCK:
            views["clock"].mode = (views["clock"].mode + 1) % views["clock"].num_modes


def encoder_dec(dummy):
    global views, encoder, mode
    cur_time = time.time()
    if (cur_time - encoder["time"]) > encoder["threshold"]:
        print("Decrementing encoder")
        encoder["time"] = time.time()
        if mode == Mode.CLOCK:
            views["clock"].mode = (views["clock"].mode - 1) % views["clock"].num_modes

def encoder_click():
    global mode, views
    if mode == Mode.CLOCK:
        mode = Mode.MENU
    elif mode == Mode.MENU:
        mode = Mode.CLOCK

def main():
    mode_time = time.time()

    my_encoder = pyky040.Encoder(CLK=4, DT=3, SW=2)
    my_encoder.setup(step=1, loop=True,
                     sw_callback=encoder_click,
                     inc_callback=encoder_inc,
                     dec_callback=encoder_dec)

    encoder_thread = threading.Thread(target = my_encoder.watch)
    encoder_thread.start()

    while(True):
        if mode == Mode.CLOCK:
            display.draw(views["clock"])
        elif mode == Mode.MENU:
            display.draw(views["menu"])

        time.sleep(0.1)


main()
