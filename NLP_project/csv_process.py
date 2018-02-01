# _*_ coding:utf-8 _*_
__author__ = "WDdeBWT"
__date__ = "2018/01/08"

import re
import csv

import jieba
import win_unicode_console
win_unicode_console.enable()

class CSV_Process:
    def __init__(self):
        self.read_path = "D:\\code\\file\\imageContent.csv"
        self.write_path = "D:\\code\\file\\output.csv"
    
    def read_csv(self):
        i = 0
        content_list = []
        with open(self.read_path) as r:
            reader = csv.reader(r)
            for row in reader:
                i += 1
                content_list.append(row)
        print("Total lines: " + str(i))
        return content_list
    
    def get_weibo_content(self, content_list):
        re_str_1 = re.compile('(\d*?)\_(\w*?)\_(\w*?)\.')
        weibo_dict = {}
        for content in content_list:
             match = re.findall(re_str_1, content[0])[0][0]
             if match:
                print(match)
                if match in weibo_dict:
                    weibo_dict[match] += content[1]
                else:
                    weibo_dict[match] = content[1]
        return  weibo_dict

    def write_csv(self, weibo_dict):
        with open(self.write_path, 'w', newline="") as w:
            csvwriter = csv.writer(w, delimiter=',')
            for item in weibo_dict:
                csvwriter.writerow((item, weibo_dict[item]))

csv_prs = CSV_Process()
content_list = tcsv_prse.read_csv()
content_list = csv_prs.get_weibo_content(content_list)
csv_prs.write_csv(content_list)
