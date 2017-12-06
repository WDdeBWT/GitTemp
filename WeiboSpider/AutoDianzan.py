# -*- coding:utf-8 -*-
import time
from selenium import webdriver


class SpiderWeike:
    def __init__(self):
        self.chrome = webdriver.Chrome()
        self.url_dianzan = 'http://zhibu.univs.cn/front/article/show/3/1929dd2bd0ab11e79b5e5254004dfc45'

    def dianzan(self):
        for i in range(1000):
            self.chrome.get(self.url_dianzan)
            self.chrome.find_element_by_xpath("//*[@id='click']").click()
            time.sleep(5)


spider = SpiderWeike()
spider.dianzan()
