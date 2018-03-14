# _*_ coding:utf-8 _*_
__author__ = "WDdeBWT"
__date__ = "2017/12/12"
# CollegeChineseCourse

import time
import random

import os
import re
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ChromeDriver:
    def __init__(self):
        self.browser = webdriver.Chrome()

    def login_index(self):
        self.browser.get(r'https://www.baidu.com/s?ie=UTF-8&wd=%E5%9E%83%E5%9C%BE%E7%84%9A%E7%83%A7')
        print(self.browser.page_source)
    

spider = ChromeDriver()
spider.login_index()