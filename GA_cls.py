#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw
import random as r
import time


class Color(object):
    def __init__(self):
        self.r = r.randint(0, 255)
        self.g = r.randint(0, 255)
        self.b = r.randint(0, 255)
        self.a = r.randint(90, 110)


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

    def mutate_from(self, parent):
        self.ax = min(max(0, parent.ax + r.randint(-15, 15)), 255)
        self.ay = min(max(0, parent.ay + r.randint(-15, 15)), 255)
        self.bx = min(max(0, parent.bx + r.randint(-15, 15)), 255)
        self.by = min(max(0, parent.by + r.randint(-15, 15)), 255)
        self.cx = min(max(0, parent.cx + r.randint(-15, 15)), 255)
        self.cy = min(max(0, parent.cy + r.randint(-15, 15)), 255)
        self.color.r = min(max(0, parent.color.r + r.randint(-20, 20)), 255)
        self.color.g = min(max(0, parent.color.g + r.randint(-20, 20)), 255)
        self.color.b = min(max(0, parent.color.b + r.randint(-20, 20)), 255)

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
    mutate_rate = 0.02
    size = (256, 256)
    size_1 = (255, 255)
    target_pixels = []

    def __init__(self):
        self.triangles = []
        self.match_rate = 0
        self.img = None

    def init_p(self):
        pass

    def add_triangles(self, num=1):
        for i in range(0, num):
            triangle = Triangle()
            self.triangles.append(triangle)

    def set_pixels(self, t):
        self.target_pixels = t

    def mutate_from_parent(self, parent):
        flag = False
        for triangle in parent.triangles:
            t = triangle
            if mutate_or_not(self.mutate_rate):
                flag = True
                a = Triangle()
                a.mutate_from(t)
                self.triangles.append(a)
                continue
            self.triangles.append(t)
        # OK We need mutate at least one at one time. It's dirty, but hmmm
        if not flag:
            self.triangles.pop()
            t = parent.triangles[r.randint(0, len(parent.triangles)-1)]
            a = Triangle()
            a.mutate_from(t)
            self.triangles.append(a)

    def calc_match_rate(self):
        if self.match_rate > 0:
            return self.match_rate
        self.match_rate = 0
        self.img = Image.new('RGBA', self.size)
        draw = ImageDraw.Draw(self.img)
        draw.polygon([(0, 0), (0, 255), (255, 255), (255, 0)], fill = (0, 0, 0, 0))
        for triangle in self.triangles:
            self.img = Image.alpha_composite(self.img, triangle.img_t or triangle.draw_it(self.size))
        pixels = [self.img.getpixel((x, y)) for x in range(0, self.size[0], 2) for y in range(0, self.size[1], 2)]
        for i in range(0, min(len(pixels), len(self.target_pixels))):
            delta_red   = pixels[i][0] - self.target_pixels[i][0]
            delta_green = pixels[i][1] - self.target_pixels[i][1]
            delta_blue  = pixels[i][2] - self.target_pixels[i][2]
            self.match_rate += delta_red   * delta_red   + \
                               delta_green * delta_green + \
                               delta_blue  * delta_blue

    def draw_it(self, i):
        self.img.save("/home/conplat/GA_engine/bb_%d_n%d_%d_128.png" % (i, len(self.triangles), int(self.mutate_rate * 100)))


def main():
    img_path = "/home/conplat/GA_engine/bb.png"
    img = Image.open(img_path).resize((256, 256)).convert('RGBA')
    size = (256, 256)
    size_1 = (255, 255)
    target_img = [img.getpixel((x, y)) for x in range(0, size[0], 2) for y in range(0, size[1], 2)]
    Canvas.target_pixels = target_img
    parent = Canvas()
    parent.add_triangles(90)
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
        if i % 1000 == 0:
            parent.draw_it(i)


if __name__ == '__main__':
    main()