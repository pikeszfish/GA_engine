## GA_engine
=========
写了个在线的版本，js写的    
[GA_engine在线版](pikeszfish.me/GA/)    
目前canvas的大小是256 *256，所以三角形的点的横纵坐标范围是[0, 255]    
颜色使用的rgba(RGB + alpha)，html中的alpha范围为0-1，rgb的范围是[0, 255]    


一个采用遗传算法利用多个三角形拟合图片的工具
像这样

![Chrome](https://raw.githubusercontent.com/pikeszfish/GA_engine/master/chrome.png)
![Chrome after 4000000](https://raw.githubusercontent.com/pikeszfish/GA_engine/master/chrome_100_1_4000000.png)


### Usage
usage: GAengine [-h] [-t TARGET] [-o FOLDER] [-n TRIANGLE_NUM] [-l LOOP] [-p RESULT_NAME]    
