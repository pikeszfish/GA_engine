#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw
# import numpy as np
# from numpy import *
import time
import random as r
path1 = '/Users/pike/CODES/GA_engine/'
# http://rogeralsing.com/2008/12/09/genetic-programming-mona-lisa-faq/


def mutate_or_not(rate):
    if rate > random.random():
        return True
    else:
        return False

def z_or_o():
    '''
        zero or one?
    '''
    return random.randint(0, 1)


def calc_rate(target_img, generation, generation_num, gene_num, size):
    for i in range(0, generation_num):
        single = generation[i]
        genes = single["genes"]
        base_img = Image.new('RGBA', size)
        base_draw = ImageDraw.Draw(base_img)
        base_draw.polygon([(0, 0), (0, size[1] - 1), (size[0] - 1, size[1] - 1), (size[0] - 1, 0)], fill = (0, 0, 0, 0))
        t1 = time.time()
        for j in range(0, gene_num):
            img = Image.new('RGBA', size)
            draw = ImageDraw.Draw(img)
            single_gene = genes[j]
            draw.polygon([(single_gene[0], single_gene[1]), \
                          (single_gene[2], single_gene[3]), \
                          (single_gene[4],single_gene[5])], \
                          fill = (single_gene[6], single_gene[7], single_gene[8], single_gene[9]))
            base_img = Image.alpha_composite(base_img, img)
        t2 = time.time()
        generation[i]["rate"] = abs(sum((array(base_img) - target_img)))

def choose(p, c):
    size = (256, 256)
    base_img = Image.new('RGBA', size)
    base_draw = ImageDraw.Draw(base_img)
    base_draw.polygon([(0, 0), (0, 255), (255, 255), (255, 0)], fill = (0, 0, 0, 0))
    t1 = time.time()
    for s in p:
        img = Image.new('RGBA', size)
        draw = ImageDraw.Draw(img)
        draw.polygon([(s[0], s[1]), \
                      (s[2], s[3]), \
                      (s[4],s[5])], \
                      fill = (s[6], s[7], s[8], s[9]))
        base_img = Image.alpha_composite(base_img, img)
    for i in base_img:
        


def calc_child(p, c):
    rate = 0.03
    for single in p:
        if mutate_or_not(rate):
            s = (r.randint(255), r.randint(255), \
                 r.randint(255), r.randint(255), \
                 r.randint(255), r.randint(255), \
                 r.randint(255), r.randint(255), \
                 r.randint(255), r.randint(255), )
        else:
            s = single
        c.append(s)

def init_parent(t):
    # (a1, a2, b1, b2, c1, c2, r, g, b, a)
    for i in range(0, 256*256)
        single = (r.randint(255), r.randint(255), \
                  r.randint(255), r.randint(255), \
                  r.randint(255), r.randint(255), \
                  r.randint(255), r.randint(255), \
                  r.randint(255), r.randint(255), )
        t.append(single)

def main():
    # size = (100, 100)
    # size_1 = (size[0] - 1, size[1] - 1)
    img_path = "/Users/pike/CODES/GA_engine/bb.png"
    target_img = Image.open(img_path).convert('RGBA')
    parent = []
    init_it(parent)
    child = []
    select_num = 500000

    for i in range(0, 500000):
        calc_child(parent, child)
        choose(parent, child)
