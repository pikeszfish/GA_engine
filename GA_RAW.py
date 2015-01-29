#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw
# import numpy as np
# from numpy import *
import time
import random as r
import numpy as np
path1 = '/Users/pike/CODES/GA_engine/'
# http://rogeralsing.com/2008/12/09/genetic-programming-mona-lisa-faq/


def mutate_or_not(rate):
    if rate > r.random():
        return True
    else:
        return False

def z_or_o():
    '''
        zero or one?
    '''
    return random.randint(0, 1)


def creat_one_pic(p, size, i):
    base_img = Image.new('RGBA', size)
    base_draw = ImageDraw.Draw(base_img)
    base_draw.polygon([(0, 0), (0, size[1] - 1), (size[0] - 1, size[1] - 1), (size[0] - 1, 0)], fill = (0, 0, 0, 0))
    t1 = time.time()
    for j in p:
        img = Image.new('RGBA', size)
        draw = ImageDraw.Draw(img)
        draw.polygon([(j[0], j[1]), (j[2], j[3]), (j[4],j[5])],\
                        fill = (j[6], j[7], j[8], 110))
        base_img = Image.alpha_composite(base_img, img)
    print ("/home/conplat/GA_engine_%d.png"%i)
    base_img.save("/home/conplat/GA_engine/GA_engine_%d.png"%i)


# def calc_rate(target_img, generation, generation_num, gene_num, size):
#     for i in range(0, generation_num):
#         single = generation[i]
#         genes = single["genes"]
#         base_img = Image.new('RGBA', size)
#         base_draw = ImageDraw.Draw(base_img)
#         base_draw.polygon([(0, 0), (0, size[1] - 1), (size[0] - 1, size[1] - 1), (size[0] - 1, 0)], fill = (0, 0, 0, 0))
#         t1 = time.time()
#         for j in range(0, gene_num):
#             img = Image.new('RGBA', size)
#             draw = ImageDraw.Draw(img)
#             single_gene = genes[j]
#             draw.polygon([(single_gene[0], single_gene[1]), \
#                           (single_gene[2], single_gene[3]), \
#                           (single_gene[4],single_gene[5])], \
#                           fill = (single_gene[6], single_gene[7], single_gene[8], single_gene[9]))
#             base_img = Image.alpha_composite(base_img, img)
#         t2 = time.time()
#         generation[i]["rate"] = abs(sum((array(base_img) - target_img)))

def choose(p, c, s):
    size = (256, 256)
    p_img = Image.new('RGBA', size)
    p_draw = ImageDraw.Draw(p_img)
    p_draw.polygon([(0, 0), (0, 255), (255, 255), (255, 0)], fill = (0, 0, 0, 0))
    t1 = time.time()
    for t in p:
        img = Image.new('RGBA', size)
        draw = ImageDraw.Draw(img)
        draw.polygon([(t[0], t[1]), \
                      (t[2], t[3]), \
                      (t[4],t[5])], \
                      fill = (t[6], t[7], t[8], t[9]))
        p_img = Image.alpha_composite(p_img, img)
    pp = [p_img.getpixel((x, y)) for x in range(0, 255, 2) for y in range(0, 255, 2)]
    # print (str(pp))
    p_rate = 0
    # p_rate = sum(list(map(lambda x, y: (x-y)*(x-y), pp, s)))
    for i in range(0, min(len(pp), len(s))):
        delta_red = pp[i][0] - s[i][0]
        delta_green = pp[i][1] - s[i][1]
        delta_blue = pp[i][2] - s[i][2]
        p_rate += delta_red * delta_red + \
                  delta_green * delta_green + \
                  delta_blue * delta_blue
    print ("p_rate: %d" % p_rate)

    c_img = Image.new('RGBA', size)
    c_draw = ImageDraw.Draw(c_img)
    c_draw.polygon([(0, 0), (0, 255), (255, 255), (255, 0)], fill = (0, 0, 0, 0))
    t1 = time.time()
    for t in c:
        img = Image.new('RGBA', size)
        draw = ImageDraw.Draw(img)
        draw.polygon([(t[0], t[1]), \
                      (t[2], t[3]), \
                      (t[4],t[5])], \
                      fill = (t[6], t[7], t[8], t[9]))
        c_img = Image.alpha_composite(c_img, img)
    cc = [c_img.getpixel((x, y)) for x in range(0, 255, 2) for y in range(0, 255, 2)]
    # print (len(cc))
    c_rate = 0
    # c_rate = sum(list(map(lambda x, y: (x-y)*(x-y), pp, s)))
    for i in range(0, min(len(cc), len(s))):
        delta_red = cc[i][0] - s[i][0]
        delta_green = cc[i][1] - s[i][1]
        delta_blue = cc[i][2] - s[i][2]
        c_rate += delta_red * delta_red + \
                  delta_green * delta_green + \
                  delta_blue * delta_blue
    print ("c_rate: %d" % c_rate)
    if p_rate < c_rate:
        print ("<")
        return p, []
    else:
        print (">")
        return c, []
    c = []

def calc_child(p):
    rate = 0.03
    c = []
    for single in p:
        if mutate_or_not(rate):
            s = (r.randint(0, 255), r.randint(0, 255), \
                 r.randint(0, 255), r.randint(0, 255), \
                 r.randint(0, 255), r.randint(0, 255), \
                 r.randint(0, 255), r.randint(0, 255), \
                 r.randint(0, 255), r.randint(0, 255), )
        else:
            s = single
        c.append(s)
    return c

def init_parent(t):
    # (a1, a2, b1, b2, c1, c2, r, g, b, a)
    for i in range(0, 120):
        single = (r.randint(0, 255), r.randint(0, 255), \
                  r.randint(0, 255), r.randint(0, 255), \
                  r.randint(0, 255), r.randint(0, 255), \
                  r.randint(0, 255), r.randint(0, 255), \
                  r.randint(0, 255), r.randint(0, 255), )
        t.append(single)

def main():
    # size = (100, 100)
    # size_1 = (size[0] - 1, size[1] - 1)
    # t1 = time.time()
    img_path = "/home/conplat/GA_engine/bb.png"
    img = Image.open(img_path).convert('RGBA')
    target_img = [img.getpixel((x, y)) for x in range(0, 255, 2) for y in range(0, 255, 2)]
    parent = []
    init_parent(parent)
    child = []
    select_num = 500000
    for i in range(1, 500000):
        print (str(i))
        child = calc_child(parent)
        parent, child = choose(parent, child, target_img)
        if i % 100 == 0:
            creat_one_pic(parent, (256, 256), i)

if __name__ == '__main__':
    main()