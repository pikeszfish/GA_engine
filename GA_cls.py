#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw
import random as r
import numpy as np
import time


class Color(object):
    def __init__(self):
        self.r = r.randint(0, 255)
        self.g = r.randint(0, 255)
        self.b = r.randint(0, 255)
        self.a = 110


class Triangle(object):
    def __init__(self, size=(255, 255)):
        self.ax = r.randint(0, size[0])
        self.ay = r.randint(0, size[1])
        self.bx = r.randint(0, size[0])
        self.by = r.randint(0, size[1])
        self.cx = r.randint(0, size[0])
        self.cy = r.randint(0, size[1])
        self.color = Color()
        self.img_t = None

    def draw_it(self, size=(256, 256)):
        self.img_t = Image.new('RGBA', size)
        draw = ImageDraw.Draw(self.img_t)
        draw.polygon([(self.ax, self.ay),  \
                      (self.bx, self.by),  \
                      (self.cx, self.cy)], \
                      fill = (self.color.r, self.color.g, self.color.b, self.color.a))
        return self.img_t


def mutate_or_not(rate):
    return True if rate > r.random() else False


class Canvas(object):
    mutate_rate = 0.06
    size = (256, 256)
    size_1 = (255, 255)
    target_pixels = []

    def __init__(self):
        self.triangles = []
        self.match_rate = 0
        self.img = None
        # self.pixels = []

    def init_p(self):
        pass

    def add_triangles(self, num=1):
        for i in range(0, num):
            triangle = Triangle()
            self.triangles.append(triangle)

    def set_pixels(self, t):
        self.target_pixels = t

    def mutate_from_parent(self, parent):
        for triangle in parent.triangles:
            t = triangle
            if mutate_or_not(self.mutate_rate):
                t = Triangle()
            self.triangles.append(t)

    def calc_match_rate(self):
        if self.match_rate > 0:
            return self.match_rate
        self.match_rate = 0
        self.img = Image.new('RGBA', self.size)
        draw = ImageDraw.Draw(self.img)
        draw.polygon([(0, 0), (0, 255), (255, 255), (255, 0)], fill = (0, 0, 0, 0))
        for triangle in self.triangles:
            self.img = Image.alpha_composite(self.img, triangle.img_t or triangle.draw_it(self.size))
        pixels = [self.img.getpixel((x, y)) for x in range(0, self.size_1[0], 2) for y in range(0, self.size_1[1], 2)]

        for i in range(0, min(len(pixels), len(self.target_pixels))):
            delta_red   = pixels[i][0] - self.target_pixels[i][0]
            delta_green = pixels[i][1] - self.target_pixels[i][1]
            delta_blue  = pixels[i][2] - self.target_pixels[i][2]
            self.match_rate += delta_red   * delta_red   + \
                               delta_green * delta_green + \
                               delta_blue  * delta_blue

    def draw_it(self, i):
        self.img.save("/home/conplat/GA_engine/GA_cls_%d.png"%i)


def main():
    img_path = "/home/conplat/GA_engine/bb.png"
    img = Image.open(img_path).convert('RGBA')
    target_img = [img.getpixel((x, y)) for x in range(0, 255, 2) for y in range(0, 255, 2)]
    Canvas.target_pixels = target_img
    parent = Canvas()
    parent.add_triangles(120)
    i = 0
    while True:
        child = Canvas()
        child.mutate_from_parent(parent)
        parent.calc_match_rate()
        child.calc_match_rate()
        print ('parent rate %d' % parent.match_rate)
        print ('child  rate %d' % child.match_rate)
        print (i)
        parent = parent if parent.match_rate < child.match_rate else child
        child = None
        i += 1
        if i % 400 == 0:
            parent.draw_it(i)


if __name__ == '__main__':
    main()