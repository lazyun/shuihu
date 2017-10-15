import pymouse

class SH_MOUSE(object):
    def __init__(self):
        self.mouse = pymouse.PyMouse()

    def click(self, x, y):
        #
        self.mouse.click(x, y, 1)


    def double_click(self, x, y):
        self.mouse.click(x, y, 1, 2)
