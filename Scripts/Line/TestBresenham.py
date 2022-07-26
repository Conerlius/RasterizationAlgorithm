#!/usr/bin/env python
# -*-coding:utf-8 -*-
import math

import cv2


# 屏幕的宽高
import numpy

screen_height = 600
screen_width = 800

# 直线相关的
begin_point = (30, 10)
end_point = (720, 500)

# 图像
img =numpy.ones((screen_height,screen_width,3),dtype=numpy.uint8)


def setPixel(x, y):
    if y >= screen_width:
        return
    if x >= screen_height:
        return
    img[y, x, 0] = 255
    img[y, x, 1] = 255
    img[y, x, 2] = 255


def LineBresenham(bpoint, epoint):
    dx = math.fabs(epoint[0] - bpoint[0])
    dy = math.fabs(epoint[1] - bpoint[1])
    p = 2 * dy - dx
    twoDy = 2 * dy
    twoDyMinusDx = 2 * (dy - dx)
    x = 0
    y = 0
    if bpoint[0] > epoint[0]:
        x = epoint[0]
        y = epoint[1]
        epoint[0] = bpoint[0]
    else:
        x = bpoint[0]
        y = bpoint[1]
    setPixel(bpoint[0], bpoint[1])
    while x < epoint[0]:
        x += 1
        if p < 0:
            p += twoDy
        else:
            y += 1
            p += twoDyMinusDx
        setPixel(x, y)


def main():
    LineBresenham(begin_point, end_point)
    cv2.imshow('img', img)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()