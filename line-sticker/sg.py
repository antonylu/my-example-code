#-*- coding:utf8 -*-
"""
sticker_gen.py

Generate sticker PNG files from text
The sticker size is:

* 370 x 320, with 10 px blank in each side
* 350 x 300, generate canvas

"""
from PIL import Image,ImageDraw,ImageFont

#font = ImageFont.truetype('simsun.ttc',24)
font = ImageFont.truetype('setofont.ttf',24)
img = Image.new('RGB',(370,320),(255,255,255))
draw = ImageDraw.Draw(img)
draw.text( (0,50), u'你好,世界!',(0,0,0),font=font)
#draw.text((0,60),str('你好','utf-8'),(0,0,0),font=font) 
img.save("test.png")
exit(0)
