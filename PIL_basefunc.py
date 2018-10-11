#!/usr/bin/python
# coding:utf-8
import os
import sys
import math
from PIL import Image, ImageDraw, ImageFont

msyh = 'fonts/msyh.ttf'

def addNewFont(font, size):
    return ImageFont.truetype(font, size)

def lengthOfChar(char, font, size):
    ###  获取文字长度
    tmp_font = ImageFont.truetype(font, size)
    char_length = tmp_font.getsize(char)[0]
    return char_length

def createNewImage(width, height, bg=(255,255,255,255), mode="RGBA"):
    ###  创建新图片
    return Image.new(mode, (width, height), bg)

def draw(image):
    ###  图片成为可写状态
    draw = ImageDraw.Draw(image)
    return draw

def draw_rectangle(draw, size, fill=None, outline=None):
    ###  绘制长方形
    draw.rectangle(size, fill=fill, outline=outline)

def draw_text(draw, text, pos, font, fontSize, fontColor='black'):
    ###  添加文字
    font = ImageFont.truetype(font, fontSize)
    draw.text(pos, text, fill=fontColor, font=font)

def draw_center_text(draw, text, pos, font, fontSize, fontColor=(0,0,0)):
    ### 给定文字的中间位置
    len_char = lengthOfChar(text, font, fontSize)
    draw_text(draw, text, (pos[0]-len_char/2, pos[1]), font, fontSize, fontColor)

def draw_polygon(draw, pos, fill=None, outline=None):
    draw.polygon(pos, fill=fill, outline=outline)

def changePicSize(image, width, height):
    ### 将图片放到固定大小的画布中央，原图片大小不变,空白处做透明处理， 即更改整个图片所占空间大小，但实际图片大小并不发生变化
    canvas = Image.new('RGBA', (width, height),(255, 255, 255, 0))
    if not isinstance(image, Image.Image):
        image = Image.open(image)
    image = image.convert('RGBA')
    img_w, img_h = image.size
    for i in range(img_w):
        for j in range(img_h):
            r, g, b, a = image.getpixel((i,j))
            if r == g == b == 255: 
                a = 0
                image.putpixel((i,j), (r, g, b, a))
    canvas.paste(image, ((width-img_w)//2, (height-img_h)//2), mask=image)
    return canvas

class pil_draw():
    def __init__(self, image):
        self.img = image
        self._draw()

    def _draw(self):
        self.draw = ImageDraw.Draw(self.img)

    def draw_arc(self, size, degree, fill=None):
        self.draw.arc(size, degree[0], degree[1], fill=fill)

    def draw_pie(self, size, degree, fill=None, outline=None):
        self.draw.pieslice(size, degree[0], degree[1], fill=fill)

    def draw_rectangle(self, size, fill=None, outline=None):
        self.draw.rectangle(size, fill=fill, outline=outline)

    def draw_polygon(self, pos, fill=None, outline=None):
        self.draw.polygon(pos, fill=fill, outline=outline)

    def draw_ring(self, size, degree, width=10, fill='blue'):
        self.draw_pie(size, degree, fill)
        size = tuple([size[0]+width, size[1]+width, size[2]-width, size[3]-width])
        self.draw_pie(size, degree, 'white')

    def draw_line(self, size, width=5, fill='blue'):
    	self.draw.line((size), width=width, fill=fill)

    def draw_text(self, text, pos, font, fontSize, fontColor='black'):
        font = ImageFont.truetype(font, fontSize)
        self.draw.text(pos, text, fill=fontColor, font=font)



if __name__ == "__main__":
    width = height = 2000
    image = Image.new("RGBA", (width,height), (255,255,255,1))
    test = pil_draw(image)
    test.draw_ring((0,0,width,height), (0,360))

    test.img.save("PIL_basefunc.png")
