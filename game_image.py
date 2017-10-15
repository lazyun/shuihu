import os
import pytesseract

from PIL import ImageGrab, Image
from pylab import *


class GAME_IM(object):
    def __init__(self, file_path):
        #self.img = Image.open(r'.\abc.jpg')
        self.im = ImageGrab.grab()

        self.file_path = file_path
        self.judge_path_exist()

    def judge_path_exist(self):
        if not os.path.exists(self.file_path):
            os.mkdir(self.file_path)


    def screenshot(self, region):
        img = ImageGrab.grab(region)
        img.save(os.path.join(self.file_path, './cur.png'))
        #img.show()


    def cut_photos(self, source, flag, region):
        # 加载原始图片
        img = Image.open(os.path.join(self.file_path, source))
        cropImg = img.crop(region)
        # 保存裁切后的图片
        cropImg.save(os.path.join(self.file_path, flag))

        #im = Image.open(os.path.join(self.file_path, flag))

        #out = im.resize((100, 100), Image.ANTIALIAS)
        #out.save(os.path.join(self.file_path, flag))


        # x, y = im.size
        # # 使用白色来填充背景 from：www.jb51.net
        # # (alpha band as paste mask).
        # p = Image.new('RGBA', im.size, (255, 255, 255))
        # p.paste(im, (0, 0, x, y), im)
        # p.save(os.path.join(self.file_path, flag))


    def read_text(self, file_name):
        text = pytesseract.image_to_string(Image.open(os.path.join(self.file_path, file_name)), lang='chi_sim')
        print(len(text), text)


    def change_img(self):
        # 灰度处理
        im = Image.open('./date/verification1.png').convert('L')
        #im.save('./date/aaa.png')

        # 增强
        from PIL import ImageEnhance
        enhancer = ImageEnhance.Sharpness(im)
        for i in range(20):
            factor = i / 4.0
            im = enhancer.enhance(factor) #.show("Sharpness %f" % factor)

        im.save('./date/aaa.png', dpi=(300.0, 300.0))

    def read_color(self):
        im = Image.open('./date/verification1.png')
        pix = im.load()
        width = im.size[0]
        height = im.size[1]
        for x in range(width):
            for y in range(height):
                print(x, y)
                print(pix[x, y]) #, end=' ')
                #r, g, b = pix[x, y]
                #print(r, g, b)
            print('\n')

        # print(im.getpixel((0, 0)))
        # img_src = im.convert('RGBA')
        # # 获得文字图片的每个像素点
        # src_strlist = img_src.load()
        #
        # # 100,100 是像素点的坐标
        # data = src_strlist[0, 0]
        # print(data)
        # data = src_strlist[0, 1]
        # print(data)

    def image_around(self):
        im = array(Image.open('./date/verification1.png').convert('L'))
        figure()
        gray()
        contour(im, origin='image')
        axis('equal')
        axis('off')
        figure()
        hist(im.flatten(), 128)
        show()


if __name__ == '__main__':
    game_img = GAME_IM('./date/')
    #game_img.change_img()
    #game_img.read_text('cur.png')
    #game_img.read_color()
    game_img.image_around()
