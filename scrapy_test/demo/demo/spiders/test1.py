# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup


class Test1Spider(scrapy.Spider):
    name = 'test1'
    start_urls = [r'https://www.baidu.com/s?ie=UTF-8&wd=%E5%9E%83%E5%9C%BE%E7%84%9A%E7%83%A7']

    def __init__(self):
        self.times = 0

    def parse(self, response):
        self.times += 1
        fname = "D:\\code\\file\\" + str(self.times) + ".html"
        with open(fname, 'wb') as w:
            w.write(response.body)
        soup = BeautifulSoup(response.body, "html.parser")
        all_href = soup.find_all('a')
        for url in all_href:
            try:
                yield scrapy.Request(url.get('href'), callback=self.parse)
            except:
                pass
