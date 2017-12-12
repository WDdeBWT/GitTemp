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
        self.username = '0121503490301'
        self.userpass = '0121503490301'
        self.URL_START = "http://59.69.102.9/zgyw/index.aspx"

    def login_index(self):
        self.browser.get(self.URL_START)

        time.sleep(5)
        elem_user = self.browser.find_element_by_id('ctl00_ContentPlaceHolder1_name')
        elem_pass = self.browser.find_element_by_id('ctl00_ContentPlaceHolder1_pwd')

        elem_user.send_keys(self.username)
        elem_pass.send_keys(self.userpass)

        time.sleep(2)

        elem_pass.send_keys(Keys.RETURN)
        time.sleep(3)
        print("--------------------login success--------------------")
        self.browser.get("http://59.69.102.9/zgyw/study/LearningIndex.aspx")
        time.sleep(3)
    
    def auto_click(self):
        click_url = random.randint(1, 6)
        waiting_time = random.randint(10, 100)
        print(click_url)
        print(waiting_time)
        try:
            if click_url == 1:
                self.browser.get("http://59.69.102.9/zgyw/study/LearningIndex.aspx")
            if click_url == 2:
                self.browser.find_element_by_id("wen").click()
            if click_url == 3:
                self.browser.find_element_by_id("shi").click()
            if click_url == 4:
                self.browser.find_element_by_id("ci").click()
            if click_url == 5:
                self.browser.find_element_by_id("qu").click()
            if click_url == 6:
                self.browser.find_element_by_id("xiaoshuo").click()
        except Exception as e:
            print(e)
        time.sleep(waiting_time)



spider = ChromeDriver()
spider.login_index()
for i in range(10):
    spider.auto_click()
print("----------")