# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from bs4 import BeautifulSoup


class Test1Spider(RedisSpider):
    name = 'test1'
    redis_key = "sinaspider:start_urls"

    def __init__(self):
        self.times = 0
    
    # def __init__(self, *args, **kwargs):
    #     domain = kwargs.pop('domain', '')
    #     self.allowed_domains = filter(None, domain.split(','))
    #     super(Test1Spider, self).__init__(*args, **kwargs)
    #     self.times = 0

    def parse(self, response):
        self.times += 1
        fname = "F:\\Files\\scrapy_test1\\" + str(self.times) + ".html"
        with open(fname, 'wb') as w:
            w.write(response.body)
        soup = BeautifulSoup(response.body, "html.parser")
        all_href = soup.find_all('a')
        for url in all_href:
            try:
                yield scrapy.Request(url.get('href'), callback=self.parse)
            except:
                pass
