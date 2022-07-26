#!/usr/bin/env python
# -*-coding:utf-8 -*-
import math

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


def LineDDA(bpoint, epoint):
    dx = epoint[0] - bpoint[0]
    dy = epoint[1] - bpoint[1]
    steps = 0
    k = 0
    xIncrement = 0.0
    yIncrement = 0.0
    x = bpoint[0]
    y = bpoint[1]
    # 最大位移方向的判定
    if math.fabs(dx) > math.fabs(dy):
        steps = math.floor(math.fabs(dx))
    else:
        steps = math.floor(math.fabs(dy))
    #x,y方向上的增量
    xIncrement = dx / steps
    yIncrement = dy / steps
    setPixel(round(x), round(y))
    for k in range(steps):
        x += xIncrement
        y += yIncrement
        setPixel(round(x), round(y))


def main():
    LineDDA(begin_point, end_point)
    cv2.imshow('img', img)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()