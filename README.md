## GA_engine
=========
一个采用遗传算法利用多个三角形拟合图片的工具   
像这样  

![Chrome](https://raw.githubusercontent.com/pikeszfish/GA_engine/master/chrome.png)
![Chrome after 4000000](https://raw.githubusercontent.com/pikeszfish/GA_engine/master/chrome_100_1_4000000.png)  


### Usage
usage: GAengine [-h] [-t TARGET] [-o FOLDER] [-n TRIANGLE_NUM] [-l LOOP] [-p RESULT_NAME]

It's a very simple program using GA(Genetic Algorithm) compositing some triangles into one image to fitting the target image.

optional arguments:   
  -h, --help            show this help message and exit  
  -t TARGET             the img U want to fitting   
  -o FOLDER             the folder to save the result   
  -l LOOP               save the result each of somegenerations (default is 1024)   
  -n TRIANGLE_NUM       number of the triangles to fitting   
  -p RESULT_NAME        prefix name of the results U want  
                        default prefix is target image's name  
                        default result name is (target image's name)_(triangles' number)_(mutate_rate)_(generation number).png

### 主要算法思想
有两个思路:  
1. 计算一个群体，然后在群体中有选择，交叉，变异的过程。其中选择的过程是直接筛选掉一部分，然后将最优秀的群体复制一份(维持群体数量并且模拟拥有优秀的基因的个体有更大的机会将自己的基因遗传给后代)  
2. 只有两个个体，parent和child，既然只有两个，那么就是一个who can who up的节奏了。参考了()

### GA_main.py
这之前其实还有一版非numpy的，但实现较差
### GA_main_thread.py
因为纯计算的加减太多，所以尝试采用多线程，实际效果没有明显提升

之前两版是早先写的，所以计算图片相似度只是采用了rgb数值与目标图片相减，而之后两版是计算差值的平方
### GA_RAW.py
主要是parent和child的差异计算方式做了修改
### GA_engine.py
面向了对象，发现部分数据可以复用，所以速度更快，结合变异率，在一代parent和child中，可以复用的量其实相当多。————多亏了python的引用