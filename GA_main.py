#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw
from numpy import *
import time

def creat_test(i):
    size = (255, 255)
    gene_num = 100
    genes = random.randint(0, 255, (gene_num, 10))
    print (genes)
    base_img = Image.new('RGBA', size)
    base_draw = ImageDraw.Draw(base_img)
    base_draw.polygon([(0, 0), (0, size[1] - 1), (size[0] - 1, size[1] - 1), (size[0] - 1, 0)], fill = (0, 0, 0, 0))
    t1 = time.time()
    for j in range(0, gene_num):
        img = Image.new('RGBA', size)
        draw = ImageDraw.Draw(img)
        single_gene = genes[j]
        draw.polygon([(single_gene[0], single_gene[1]), (single_gene[2], single_gene[3]), (single_gene[4],single_gene[5])],\
                        fill = (single_gene[6], single_gene[7], single_gene[8], 120))
        base_img = Image.alpha_composite(base_img, img)
    print ("/home/conplat/GA_engine/test_%d.png"%i)
    base_img.save("/home/conplat/GA_engine/test_%d.png"%i)

def creat_one_pic(generation, gene_num, size, i):
    single = generation[1]
    genes = single['genes']
    base_img = Image.new('RGBA', size)
    base_draw = ImageDraw.Draw(base_img)
    base_draw.polygon([(0, 0), (0, size[1] - 1), (size[0] - 1, size[1] - 1), (size[0] - 1, 0)], fill = (0, 0, 0, 0))
    t1 = time.time()
    for j in range(0, gene_num):
        img = Image.new('RGBA', size)
        draw = ImageDraw.Draw(img)
        single_gene = genes[j]
        draw.polygon([(single_gene[0], single_gene[1]), (single_gene[2], single_gene[3]), (single_gene[4],single_gene[5])],\
                        fill = (single_gene[6], single_gene[7], single_gene[8], 120))
        base_img = Image.alpha_composite(base_img, img)
    print ("/home/conplat/GA_engine_%d.png"%i)
    base_img.save("/home/conplat/GA_engine/aa_%d.png"%i)

def mutate_or_not(rate):
    if rate > random.random():
        return True
    else:
        return False

def f_or_m():
    '''
        alike father or mother ?
    '''
    return random.randint(0, 1)

def crossover_generation_complex(generation, generation_num, gene_num, gene_mutation_rate):
    lo = generation_num
    while lo:
        f_single = generation.pop(0)
        f_genes = f_single["genes"]
        lo = lo - 1
        m_single = generation.pop(random.randint(0, lo))
        m_genes = m_single["genes"]
        lo = lo - 1
        ran = random.randint(gene_num)
        f = array(f_genes[0])
        m = array(m_genes[0])
        for i in range(1, gene_num):
            if mutate_or_not(gene_mutation_rate):
                f_genes[i] = hstack((random.randint(0, 100, (1, 6)), random.randint(0, 100, (1, 4))))
                m_genes[i] = hstack((random.randint(0, 100, (1, 6)), random.randint(0, 100, (1, 4))))
            if f_or_m():
                f = vstack((f, f_genes[i]))
                m = vstack((m, m_genes[i]))
            else:
                f = vstack((f, m_genes[i]))
                m = vstack((m, f_genes[i]))
        generation.append({"rate": 0, "genes":f})
        generation.append({"rate": 0, "genes":m})



def select_generation(generation, generation_num, kick_out, copy_best):
    generation = generation[0:generation_num-kick_out]
    for i in range(0, kick_out):
        ran = random.randint(copy_best)
        genes = generation[ran]["genes"].copy()
        generation.append({"rate": 0, "genes": genes})

def sort_generation(generation):
    generation.sort(key=lambda x: x["rate"])

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
            draw.polygon([(single_gene[0], single_gene[1]), (single_gene[2], single_gene[3]), (single_gene[4],single_gene[5])],\
                            fill = (single_gene[6], single_gene[7], single_gene[8], 120))
            base_img = Image.alpha_composite(base_img, img)
        t2 = time.time()
        generation[i]["rate"] = abs(sum((array(base_img) - target_img)))

def init_generation(generation, generation_num, gene_num, size):
    for i in range(0, generation_num):
        a = random.randint(0, 100, (gene_num, 6))
        b = random.randint(0, 255, (gene_num, 4))
        genes = hstack((a, b))
        single = {"rate": 0, "genes": genes}
        generation.append(single)

def main():
    select_num = 5000
    generation_num = 120
    gene_num = 100
    generation = []
    select_rate = 0.1
    gene_mutation_rate = 0.05
    size = (100, 100)
    size_1 = (size[0] - 1, size[1] - 1)
    img_path = "/home/conplat/GA_engine/bb.png"
    target_img = array(Image.open(img_path).resize(size).convert('RGBA'))
    init_generation(generation, generation_num, gene_num, size)


    # a = random.randint(0, 100, (gene_num, 10))
    # print (a * array([0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 1, 1, 1, 1]))
    # array([[0.39], [0.39], [0.39], [0.39], [0.39], [0.39], [1], [1], [1], [1]])




    for i in range(0, select_num):
        calc_rate(target_img, generation, generation_num, gene_num, size)
        sort_generation(generation)
        if i % 40 == 0:
            creat_one_pic(generation, gene_num, size, i)
            print (str(generation[0]))
        # for i in range(0, generation_num):
        #     print (generation[i]["rate"])
        kick_out = int(generation_num * select_rate)
        copy_best = int(generation_num * select_rate * 2)
        select_generation(generation, generation_num, kick_out, copy_best)
        crossover_generation_complex(generation, generation_num, gene_num, gene_mutation_rate)
        print (len(generation))
if __name__ == "__main__":
    main()

