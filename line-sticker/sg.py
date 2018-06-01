#-*- coding:utf8 -*-
"""
sticker_gen.py

Generate sticker PNG files from text
The sticker size is:

* 370 x 320, with 10 px blank in each side
* 350 x 300, generate canvas

Requirements:
* fit the size 350x300
* font size as big as possible, minimum size is 70
* all chars must fit in the canvas
* align in center
* breaks to two lines automatically

"""
from PIL import Image,ImageDraw,ImageFont


if __name__ == '__main__':
    #font = ImageFont.truetype('simsun.ttc',24)
    font = ImageFont.truetype('setofont.ttf',70)
    img = Image.new('RGBA',(370,320),(255,255,255,0))
    draw = ImageDraw.Draw(img)
    draw.text( (10,50), '你好,世界!',(0,0,0),font=font)
    img.save("test.png")
