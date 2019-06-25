from pynput.mouse import Button, Controller
import time


def click_screen_position(xy):
   x = xy[0]
   y = xy[1]
   time.sleep(2)
   mouse = Controller()
   mouse.position = (x,y)
   mouse.click(Button.left,1)


