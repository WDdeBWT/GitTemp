# _*_ coding:utf-8 _*_
__author__ = "WDdeBWT"
__date__ = "2018/01/08"

import re
import csv

import jieba
import jieba.analyse
import jieba.posseg as pseg
import win_unicode_console
from mssql_connecter import MSSQL
win_unicode_console.enable()

class MergeImgContent:
    def __init__(self):
        self.read_path = "D:\\code\\file\\imageContent.csv"
        self.write_path = "D:\\code\\file\\outputByMergeImgContent.csv"
    
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


class CsvProcesser:
    def __init__(self):
        self.read_path = "D:\\code\\file\\outputByMergeImgContent.csv"
        self.write_path = "D:\\code\\file\\outputByCsvProcesser.csv"
        self.sql = "SELECT * FROM main_imf"
    
    def read_csv(self):
        i = 0
        content_list = []
        with open(self.read_path) as r:
            reader = csv.reader(r)
            for row in reader:
                content_list.append(row)
        return content_list
    
    def merge_sql_csv(self):
        ctt_list = []
        result_list = []
        ms_sql = MSSQL()
        results = ms_sql.ExecQuery(self.sql)
        ms_sql.close_connection()
        content_list = self.read_csv()
        # Convert content_list[0] to int and sava to ctt_list
        for ctt in content_list:
            ctt_list.append((int(ctt[0]), ctt[1]))
        # Merge ctt_list and results to result_list by content_id
        for result in results:
            flag = 0
            temp = int(result[0])
            for ctt in ctt_list:
                if (ctt[0] + 2) == temp:
                    falg = 1
                    # ID, weibo content, img content, comment count, like count
                    result_list.append((result[0], result[1], ctt[1], result[6], result[7]))
                    break
            if flag == 0:
                # ID, weibo content, img content(null), comment count, like count
                result_list.append((result[0], result[1], "Null", result[6], result[7]))
        # Write to new csv
        self.write_csv(result_list)
    
    def write_csv(self, result_list):
        with open(self.write_path, 'w', newline="") as w:
            csvwriter = csv.writer(w, delimiter=',')
            for item in result_list:
                csvwriter.writerow(item)
            print("Finish")


class WordProcesser:
    def __init__(self):
        self.read_path = "D:\\code\\file\\outputByCsvProcesser.csv"
        self.write_path_1 = "D:\\code\\file\\outputByWordProcesser.csv"
        self.write_path_2 = "D:\\code\\file\\outputByWordProcesserWithStop.csv"
        self.stop_path = "D:\\code\\GitTemp\\NLP_project\\stopWordCh.txt"
    
    def read_csv(self):
        i = 0
        content_list = []
        with open(self.read_path) as r:
            reader = csv.reader(r)
            for row in reader:
                content_list.append(row)
        return content_list
    
    def get_word(self):
        temp = ""
        all_words = []
        list1 = [] #block list after jieba
        list2 = [] #line list after jieba
        content_list = self.read_csv()
        for line in content_list:
            list1 = []
            for block in line:
                temp = ""
                words = pseg.cut(block)
                for word, flag in words:
                    if flag in ('n', 'ns', 'nt', 'nz', 'an', 'vn', 'un'):
                        print(word)
                        temp += word
                        all_words.append((word, ""))
                list1.append(temp)
            list2.append(list1)
        self.write_csv(all_words, self.write_path_1)

    
    def get_word_stop(self):
        temp = ""
        all_words = []
        list1 = [] #block list after jieba
        list2 = [] #line list after jieba
        content_list = self.read_csv()
        stopwords = []
        stopword = (line.strip() for line in open(self.stop_path, 'r', encoding='UTF-8').readlines())
        for word in stopword:
            stopwords.append(word)
        for line in content_list:
            list1 = []
            for block in line:
                temp = ""
                words = pseg.cut(block)
                for word, flag in words:
                    if flag in ('n', 'ns', 'nt', 'nz', 'an', 'vn', 'un'):
                        if word not in stopwords:
                            print(word)
                            temp += word
                            all_words.append((word, ""))
                list1.append(temp)
            list2.append(list1)
        self.write_csv(all_words, self.write_path_2)
    
    def write_csv(self, result_list, write_path):
        with open(write_path, 'w', newline="") as w:
            csvwriter = csv.writer(w, delimiter=',')
            for item in result_list:
                csvwriter.writerow(item)
            print("Finish")


wp = WordProcesser()
wp.get_word()
wp.get_word_stop()

