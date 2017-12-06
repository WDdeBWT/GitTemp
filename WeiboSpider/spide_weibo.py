# -*- coding:utf-8 -*-
import time

from lxml import etree

import re
import sys
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from tools import Tools
from entitys import Person, Weibo


class SpiderWeibo:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.username = '15071306953'
        self.userpass = '19971027'
        self.url_login = 'https://passport.weibo.cn/signin/login'

    def login_weibo(self):
        self.browser.get(self.url_login)

        time.sleep(2)
        elem_user = self.browser.find_element_by_id('loginName')
        elem_pass = self.browser.find_element_by_id('loginPassword')

        elem_user.send_keys(self.username)
        elem_pass.send_keys(self.userpass)

        time.sleep(5)

        elem_pass.send_keys(Keys.RETURN)
        time.sleep(8)

        print("-------------------login success------------------")

    def Get

    def spide_base_message(self, url):
        # url_fanbb = 'https://weibo.cn/fbb0916'
        url_fanbb = url
        pattern = re.compile('\[(.*?)\]')

        try:
            self.browser.get(url_fanbb)

            selector = etree.HTML(self.browser.page_source)
            name = selector.xpath(
                '/html/body/div[4]/table/tbody/tr/td[2]/div/span[1]/text()')[0].encode('utf-8')

            num_weibo = selector.xpath(
                '/html/body/div[4]/div/span/text()')[0].encode('utf-8')
            num_watch = selector.xpath(
                '/html/body/div[4]/div/a[1]/text()')[0].encode('utf-8')
            num_fans = selector.xpath(
                '/html/body/div[4]/div/a[2]/text()')[0].encode('utf-8')

            num_weibo = re.findall(pattern, num_weibo)[0]
            num_watch = re.findall(pattern, num_watch)[0]
            num_fans = re.findall(pattern, num_fans)[0]

            aperson = Person(name, num_weibo, num_watch, num_fans)

            # call the method to write the messae of person into file

            print('-------------------aperson-------------')
            print(aperson)
            Tools.write_aperson(aperson)

        except Exception as e:
            print(e)

    def spide_weibo_messge(self, url, panname):

        selector = etree.HTML(self.browser.page_source)
        pattern = re.compile('\[(.*?)\]')
        num_weibo = selector.xpath(
            '/html/body/div[4]/div/span/text()')[0].encode('utf-8')
        num_weibo = re.findall(pattern, num_weibo)[0]
        if num_weibo == "0":
            print("----NoContent----")
            return 0

        pages = 2

        try:
            for i in range(pages):
                # url_fanbb = 'https://weibo.cn/fbb0916'
                url_fanbb = url
                print("--------------page%d-------------" % (i))
                if i != 1:
                    url_fanbb = url_fanbb + "?page=" + str(i)

                    # collect the weibo in this page
                print(url_fanbb)

                self.browser.get(url_fanbb)
                time.sleep(1)
                soup = BeautifulSoup(self.browser.page_source)

                results = soup.find_all("div", class_="c")
                #results = soup.find_all("span", class_="ctt")

                for result in results:
                    if not result.find_all("span", class_="ctt"):
                        continue

                    p_like = re.compile('赞\[(.*?)\].*?转发\[(.*?)\].*?评论\[(.*?)\]' +
                                        '.*?ct">(.*?)</span>')

                    # 0:num_like, 1:num_resend, 2:num_comment, 3: num_time
                    res_num = re.findall(p_like, str(result))[0]
                    print(res_num)
                    send_time = res_num[3].decode('utf-8')
                    # search the content
                    content = result.find_all("span", class_="ctt")[0]
                    print(content.text)

                    # need store the weibo_messge to the file
                    aweibo = Weibo(panname, send_time, content.text, res_num[0].decode(
                        'utf-8'), res_num[1].decode('utf-8'), res_num[2].decode('utf-8'))
                    Tools.write_aweibo(aweibo)

        except Exception as e:
            print(e)

    def get_bigman_fans(self, file_path):
        url_fans = "https://weibo.cn/1537790411/fans?page="
        nli = []
        ali = []
        for i in range(20):
            try:
                this_url = url_fans + str(i + 1)
                self.browser.get(this_url)
                this_html = self.browser.page_source
                soup = BeautifulSoup(this_html, "html.parser")
                all_htl = soup.find_all('td', valign="top")
                for htl in all_htl:
                    all_a = htl.find_all('a')
                    if all_a[0].text:
                        fan_name = all_a[0].text
                        if fan_name not in nli:
                            ali.append(str(all_a[0]['href']).decode('utf-8'))
                            nli.append(fan_name)
                            print(fan_name)
                            print(str(all_a[0]['href']).decode('utf-8'))
                            # 调用后两个函数，分析大V的粉丝（传入粉丝个人首页url）
                            self.spide_base_message(
                                str(all_a[0]['href']).decode('utf-8'))
                            self.spide_weibo_messge(
                                str(all_a[0]['href']).decode('utf-8'), fan_name)
                print("i:" + str(i + 1))
                time.sleep(3)
            except TimeoutException:
                print("---timeout---" + str(i + 1))
                self.browser.get(this_url)
                time.sleep(10)
            except Exception as e:
                print(e)
        with open(file_path, 'w') as f:
            for item in ali:
                f.write(item.encode('utf-8') + "\n")
                # csv输出在编码格式上还有bug，暂时不用
                # with open(file_path, "w") as csvfile:
                #     writer = csv.writer(csvfile)
                #     for item in li:
                #         writer.writerow(item.encode('gbk'))


spider = SpiderWeibo()
spider.login_weibo()
#spider.spide_base_message()
#spider.spide_weibo_messge()
spider.get_bigman_fans("test01.txt")
