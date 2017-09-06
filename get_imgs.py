#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" soccer bet main function file """

__author__ = 'ggstar'

import spider
import portfoliomodel
import time
import sys
import os


reload(sys)
sys.setdefaultencoding('utf8')

#----------------------------------------------------------
url      = 'http://www.yqimh.net/shaonvmanhua/6119_'
url_end  = '.html'
img_num  = 211
pic_name = 'whats'
#----------------------------------------------------------

#http://www.yqimh.net/shaonvmanhua/6119_6.html
#http://pic.qdanc.com/2015/6119/yaoqi6.jpg
def get_img(url,folder):
	content = spider.url_get(url)
	re_con  = re.compile(r'http.*?jpg')
	img_url = re_con.findall(content)
	os.system('wget '+img_url+' -P '+folder)

def get_urls():
	for i in range(1,img_num+1):
		get_img(url+str(i)+url_end,'./'+pic_name)


