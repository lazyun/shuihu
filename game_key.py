import pykeyboard

class SH_KEY(object):
    def __init__(self):
        self.keyboard = pykeyboard.PyKeyboard()

    def alt_e(self):
        self.keyboard.press_key(self.keyboard.alt_key)
        self.keyboard.tap_key('E')
        self.keyboard.release_key(self.keyboard.alt_key)


    def alt_q(self):
        self.keyboard.press_key(self.keyboard.alt_key)
        self.keyboard.tap_key('Q')
        self.keyboard.release_key(self.keyboard.alt_key)