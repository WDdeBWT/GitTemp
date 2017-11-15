"""
actions in this script:
1. read the json file to get parameter info
2. use webdrive to open the account history home page, the session and
   cookies are then saved.
3. open the account posts by making requests to getmsg
4. loop over the getmsg page until no more message to load
5. save message to csv file in the same directory of the json file
"""
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
    return _CHROME.find_element_by_xpath('.//body').text


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
    html_list = []
    for i in range(1000):
        msg_url = construct_message_url(account_info, i)
        _CHROME.get(msg_url)
        print(_CHROME.find_element_by_xpath('.//body').text)

        read_page_content(msg_url)
        


def save_messages_to_csv(messages, account_json_path):
    """ save messages into csv """
    path, name = os.path.split(os.path.abspath(account_json_path))
    output_csv = os.path.join(path, '{}.csv'.format(name.split('.')[0]))

    with open(output_csv, 'w', encoding='utf-8') as outfile:
        outfile.write('publish time, title, url\n')

        for msg in messages:
            # get message posting time
            try:
                pub_timestamp = msg.get('comm_msg_info').get('datetime')
                pub_dt = str(datetime.utcfromtimestamp(pub_timestamp))

                title = msg.get('app_msg_ext_info').get('title')
                url = msg.get('app_msg_ext_info').get('content_url')

                outfile.write('{}, {}, {}\n'.format(pub_dt, title, url))
            except (KeyError, AttributeError) as e:
                pass


def main(account_json):
    # account_info = get_account_info(account_json)
    account_info = {
	"__biz": "MjM5NzE0Mzg2OQ==",
	"uin": "MjQ2MDQxNzc2MA%3D%3D",
	"key": "7748b3d6c7704adc444c90f371dfdcf29ed90f65d91011c819df29c7ac49420b3afa3d377834a79890a48cd374da50cb8988e5782ccc79d115dbb368118bd67c4b673d76b52c231e94474ea145039130",
	"pass_ticket": r"jiMEhLl0qnQvfW4pkmCCrGlOiwYI6uoP2EC8r7ALtFYOtTaRe67bDqROfipCQd%2Fg"}
    home_url = construct_home_url(account_info)
    _CHROME.get(home_url)
    html_list = get_all_messages(account_info)
    print('{} messages collected'.format(len(messages)))
    print('This is the most recent one:')
    print(messages[0])

    save_messages_to_csv(messages, account_json)


if __name__ == '__main__':
    import sys
    # account_info = sys.argv[1]
    # main(account_info)
    main(None)
