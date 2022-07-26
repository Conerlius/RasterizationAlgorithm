#!/usr/bin/env python
# -*-coding:utf-8 -*-

import cv2
import numpy

# 屏幕的宽高
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


def CircleEighth(bpoint, epoint)
    pass


def main():
    CircleEighth(begin_point, end_point)
    cv2.imshow('img', img)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()