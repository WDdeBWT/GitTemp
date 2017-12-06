"""
actions in this script:
1. read the json file to get parameter info
2. use webdrive to open the account history home page, the session and
   cookies are then saved.
3. open the account posts by making requests to getmsg
4. loop over the getmsg page until no more message to load
5. save message to csv file in the same directory of the json file
"""
import time
import json
from selenium import webdriver
import os
from datetime import datetime


_CHROME = webdriver.Chrome()
_ROOT = 'https://mp.weixin.qq.com/mp/profile_ext?'


def get_account_info(info_json):
    with open(info_json, 'r', encoding='utf-8') as infile:
        d = json.load(infile)

        # make sure all the keys are there and not empty
        assert d['__biz'] not in (None, '')
        assert d['uin'] not in (None, '')
        assert d['key'] not in (None, '')
        assert d['pass_ticket'] not in (None, '')

        return d


def read_page_content(url):
    """ read url body content """
    _CHROME.get(url)
    content = []
    content.append(_CHROME.page_source)
    content.append(_CHROME.find_element_by_xpath('.//body').text)
    return content


def construct_home_url(account_info):
    __biz = '__biz={}'.format(account_info['__biz'])
    uin = 'uin={}'.format(account_info['uin'])
    key = 'key={}'.format(account_info['key'])
    pass_ticket = 'pass_ticket={}'.format(account_info['pass_ticket'])

    params = ['action=home', __biz, uin, key, pass_ticket, 'scene=124',
              'devicetype=Windows+10', 'version=6204014f', 'lang=en',
              'a8scene=7', 'winzoom=1']

    return _ROOT + '&'.join(params)


def construct_message_url(account_info, offset=0):
    """ once home is loaded, only __biz is needed for getmsg """
    __biz = '__biz={}'.format(account_info['__biz'])
    params = ['action=getmsg', __biz, 'offset={}'.format(offset), 'f=html']

    return _ROOT + '&'.join(params)


def get_all_messages(account_info):
    url_list = []
    html_list = []
    text_list = []
    for i in range(10):
        msg_url = construct_message_url(account_info, i)
        _CHROME.get(msg_url)
        # id = 1000000543 - i
        # xpath = '//*[@id=\"WXAPPMSG' + str(id) + '\"]/div/h4' # //*[@id="WXAPPMSG1000000459"]/div/h4
        # element = _CHROME.find_element_by_xpath(xpath)
        # element = _CHROME.find_element_by_xpath('//*[@id="WXAPPMSG1000000543"]/div/h4') # The first day
        element = _CHROME.find_elements_by_class_name('weui_media_title')
        for j in range(3):
            if "早读" in element[j].text:
                page_url = element[j].get_attribute('hrefs')
                if page_url not in url_list:
                    url_list.append(page_url)
                    content = read_page_content(page_url)
                    html_list.append(content[0])
                    text_list.append(content[1])
                    print(content[0][:50])
                    print(content[1][:50])
                    print(i)
                    print("-------------------")
                    break
        time.sleep(3)
    newcontent = []
    newcontent.append(html_list)
    newcontent.append(text_list)
    return newcontent


def save_messages_to_txt(newcontent, PATH):
    """ save messages into txt """
    i = 0
    for html in newcontent[0]:
        i = i + 1
        path_html = os.path.join(PATH, str(i) + "_html.txt")
        with open(path_html, "w", encoding='utf-8') as w:
            w.write(html)
    print("---Write html finished---")
    i = 0
    for text in newcontent[1]:
        i = i + 1
        path_text = os.path.join(PATH, str(i) + "_text.txt")
        with open(path_text, "w", encoding='utf-8') as w:
            w.write(text)
    print("---Write text finished---")


def main():
    # account_info = get_account_info(account_json)
    PATH = "C:\\001\\"
    account_info = {
	"__biz": "MTg1MjI3MzY2MQ==",
	"uin": "MjQ2MDQxNzc2MA%3D%3D",
	"key": "4f44f0a7d9d02374fc2ebc3a11307b9bcb1e241dd9a4e967deb4677e12a4d1f451d790f112f965e86902a327aee4055fc6164d6c71566d580fb059cfc5d2f20c1cfd225ea6d33be6c6c85bf56fa9b8b6",
	"pass_ticket": r"n93rx30W7yFA%2Bh%2BEb2IGUz1bXv%2FZADrBYbnmpwSiDYhnsPUFaIrSGVDFX4EPwlGD"}
    home_url = construct_home_url(account_info)
    _CHROME.get(home_url)
    newcontent = get_all_messages(account_info)
    save_messages_to_txt(newcontent, PATH)


if __name__ == '__main__':
    import sys
    main()
