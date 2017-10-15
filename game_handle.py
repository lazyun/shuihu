import win32api
import win32gui
import win32com
import win32con
import time

from game_key import SH_KEY
from game_image import GAME_IM

class GAME(object):
    def __init__(self):
        self.game = None
        self.start_position = None
        self.key = SH_KEY()
        self.image = GAME_IM('./date/')

        self.get_tital_handle()
        self.get_space()


    def get_tital_handle(self):
        handle_list = []
        win32gui.EnumWindows(lambda h, p: p.append(h), handle_list)
        self.game = list(filter(lambda h: 1 if '20171009' in win32gui.GetWindowText(h) else 0, handle_list ) )[0]


    def get_space(self):
        rt = win32gui.GetWindowRect(self.game)
        self.start_position = rt#[:2]


    def show_wind(self):
        if win32gui.IsIconic(self.game):
            win32gui.ShowWindow(self.game, win32con.SW_SHOW)
        win32gui.SetForegroundWindow(self.game)


    def show_package(self):
        self.show_wind()
        self.key.alt_e()


    def show_task(self):
        self.show_wind()
        self.key.alt_q()


    def game_screenshot(self):
        self.show_wind()
        time.sleep(0.5)
        self.image.screenshot(self.start_position)


    def find_verification(self):
        region = (143, 256, 396, 286)
        region = (53, 531, 360, 586)
        region = (226, 260, 255, 288)
        region = (226, 260, 252, 288)
        self.image.cut_photos('cur.png', 'verification1.png', region)
        self.image.read_text('verification1.png')




if __name__ == '__main__':
    one = GAME()
    #one.show_package()
    #one.get_space()
    #one.game_screenshot()
    one.find_verification()
    #one.image.read_text('cur.png')