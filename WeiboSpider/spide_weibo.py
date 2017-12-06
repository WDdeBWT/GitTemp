# _*_ coding:utf-8 _*_
__author__ = "WDdeBWT"
__date__ = "2017/12/06"

import time

from lxml import etree

import os
import re
import sys
import csv
import urllib
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SpiderWeibo:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.username = '15071306953'
        self.userpass = '19971027'
        self.url_login = 'https://passport.weibo.cn/signin/login'
        self.file_path = "F:\\Files\\weibo_taobaibai"

    def login_weibo(self):
        self.browser.get(self.url_login)

        time.sleep(3)
        elem_user = self.browser.find_element_by_id('loginName')
        elem_pass = self.browser.find_element_by_id('loginPassword')

        elem_user.send_keys(self.username)
        elem_pass.send_keys(self.userpass)

        time.sleep(2)

        elem_pass.send_keys(Keys.RETURN)
        time.sleep(8)

        print("--------------------login success--------------------")


    def get_main_ifmt(self):
        pages = 52
        weibo_id = 1
        try:
            for i in range(pages):
                url_index = 'https://weibo.cn/u/6003325152?filter=1'
                url_index = url_index + "&page=" + str(i+1)
                print("--------------------page:" + str(i+1) + "--------------------")
                print(url_index)

                # collect the weibo in this page
                self.browser.get(url_index)
                time.sleep(3)
                soup = BeautifulSoup(self.browser.page_source, "html.parser")

                results = soup.find_all("div", class_="c")
                if not results:
                    continue
                for result in results:
                    try:
                        if not result.find_all("span", class_="ctt"):
                            continue
                        # search the content
                        weibo_id += 1
                        print("--------------------weibo_id:" + str(weibo_id) + "--------------------")
                        content = result.find_all("span", class_="ctt")[0]
                        all_a = result.find_all("a")
                        # get url_img and url_cmt
                        flag = 0
                        for one_a in all_a:
                            if "组图" in one_a.text:
                                flag = 1
                                self.get_all_img(weibo_id, one_a["href"])
                            if "原图" in one_a.text:
                                if flag == 1:
                                    continue
                                self.get_one_img(weibo_id, one_a["href"])
                            if "评论" in one_a.text:
                                url_cmt = one_a["href"]
                                cmt = self.get_all_cmt(weibo_id, url_cmt)
                        save_path = os.path.join(self.file_path, "content")
                        save_path = os.path.join(save_path, str(weibo_id) + "_ctt.txt")
                        print(content.text)
                        f = open(save_path, 'w', encoding='utf-8')
                        f.write(content.text)
                        f.close()
                        # temp sleep
                        # time.sleep(1)
                    except Exception as e:
                        print(e)
        except Exception as e:
            print(e)
        print("--------------------运行结束，当前时间：" + str(time.strftime('%Y-%m-%d',time.localtime(time.time()))) + "--------------------")

    def get_one_img(self, weibo_id, img_url):
        print("img_url:" + img_url)
        self.browser.get(img_url)
        time.sleep(3)
        soup = BeautifulSoup(self.browser.page_source, "html.parser")
        img_src = soup.find_all("img")[0]["src"]
        ext = img_src.split('.')[-1]
        save_path = os.path.join(self.file_path, "image")
        save_path = os.path.join(save_path, str(weibo_id) + "_oig." + ext)
        #保存图片数据
        data = urllib.request.urlopen(img_src).read()
        f = open(save_path, 'wb')
        f.write(data)
        f.close()

    def get_all_img(self, weibo_id, img_url):
        print("img_url:" + img_url)
        self.browser.get(img_url)
        time.sleep(3)
        soup = BeautifulSoup(self.browser.page_source, "html.parser")
        all_img_a = soup.find_all("a")
        i = 0
        for img_a in all_img_a:
            if "原图" in img_a.text:
                i += 1
                self.browser.get("http://weibo.cn" + img_a["href"])
                time.sleep(3)
                newsoup = BeautifulSoup(self.browser.page_source, "html.parser")
                img_src = newsoup.find_all("img")[0]["src"]
                ext = img_src.split('.')[-1]
                save_path = os.path.join(self.file_path, "image")
                save_path = os.path.join(save_path, str(weibo_id) + "_aig_" + str(i) + "." + ext)
                #保存图片数据
                data = urllib.request.urlopen(img_src).read()
                f = open(save_path, 'wb')
                f.write(data)
                f.close()


    
    def get_all_cmt(self, weibo_id, cmt_url):
        print("cmt_url:" + cmt_url)
        return 0

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
spider.get_main_ifmt()
