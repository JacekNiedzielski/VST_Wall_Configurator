# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 15:19:46 2021

@author: x
"""
from PIL import Image

img1 = Image.open("img1.jpg")

img2 = Image.open("Rebars_Icons/rebar_40.png")



back_im = img1.copy()





back_im.paste(img2, box = (88,88))

back_im.save("img3.jpg", quality=100)

height_in_mm = 400
width_in_mm = 248


def mm_to_pixel(segment_mm):
    segment_pix = (segment_mm/10)*0.026458333

    return segment_pix











