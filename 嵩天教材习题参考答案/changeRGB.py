#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 15:12:37 2018

@author: weizhong
"""
from PIL import Image
from PIL import ImageEnhance
im = Image.open("/home/weizhong/Pictures/p1.jpg")
r,g,b = im.split()
om = Image.merge("RGB",(b,r,g))
om = ImageEnhance.Contrast(om)
om.enhance(20).save('/home/weizhong/Pictures/p1GBR4.jpg')
