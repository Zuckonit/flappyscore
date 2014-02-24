#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
from PIL import Image, ImageDraw, ImageFont


MEDAL_BRONZE = './img/bronze.jpg'
MEDAL_SILVER = './img/silver.jpg'
MEDAL_GOLD   = './img/gold.jpg'
MEDAL_PLATINUM = './img/platinum.jpg'
BACKGROUND_IMG = './img/bg.jpg'
FONT_SCORE = './fonts/04B_19__.TTF'


def imagecopy (dst_im, src_im, dst_x, dst_y, src_x, src_y, src_w, src_h): 
    src_im_crop = src_im.crop((src_x, src_y, src_x + src_w, src_y + src_h)) 
    dst_im.paste(src_im_crop, (dst_x, dst_y)) 
    return True 


def medal(dst_img, s):
    src_img = None
    if 10 <= s < 20:
        src_img  = Image.open(MEDAL_BRONZE)
    elif 20 <= s < 30:
        src_img = Image.open(MEDAL_SILVER)
    elif 30 <= s < 40:
        src_img = Image.open(MEDAL_GOLD)
    elif s >= 40:
        src_img = Image.open(MEDAL_PLATINUM)
    if src_img is not None:
        imagecopy(dst_img, src_img, 126, 384, 0, 0, 99, 102)
    return dst_img


def score(src_img, s):
    size = 36
    x, y, offset_y, offset = 494, 364, 93, 2
    color_outline = (2, 2, 2)
    color_font    = (254, 254, 254)
    font = ImageFont.truetype(FONT_SCORE, size)
    draw = ImageDraw.Draw(src_img)
    draw.text((x-offset, y-offset), "%d"%s, color_outline, font=font)
    draw.text((x+offset, y-offset), "%d"%s, color_outline, font=font)
    draw.text((x-offset, y+offset), "%d"%s, color_outline, font=font)
    draw.text((x+offset, y+offset), "%d"%s, color_outline, font=font)

    draw.text((x-offset, y-offset+offset_y), "%d"%s, color_outline, font=font)
    draw.text((x+offset, y-offset+offset_y), "%d"%s, color_outline, font=font)
    draw.text((x-offset, y+offset+offset_y), "%d"%s, color_outline, font=font)
    draw.text((x+offset, y+offset+offset_y), "%d"%s, color_outline, font=font)

    draw.text((x, y), "%d"%s,color_font, font=font)
    draw.text((x, y+offset_y), "%d"%s, color_font, font=font)


def generate(s, f='./score.jpg'):
    f = os.path.expanduser(f)
    source = Image.open(BACKGROUND_IMG)
    medal(source, s)
    score(source, s)
    source.save(f)
    return source

if __name__ == '__main__':
    test_score = 108
    source = generate(test_score)
    try:
        source.show()
    except:
        pass

