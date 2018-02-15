# _*_ coding:utf-8 _*_
__author__ = "WDdeBWT"
__date__ = "2018/01/08"

import re
import csv

import jieba
import jieba.analyse
import jieba.posseg as pseg
import win_unicode_console
win_unicode_console.enable()

class CsvProcesser:
    def read_csv(self, read_path):
        i = 0
        content_list = []
        with open(read_path) as r:
            reader = csv.reader(r)
            for row in reader:
                content_list.append(row)
                i += 1
        print("Read total line: " + str(i))
        return content_list
        
    def write_csv(self, result_list, write_path):
        with open(write_path, 'w', newline="") as w:
            csvwriter = csv.writer(w, delimiter=',')
            for item in result_list:
                csvwriter.writerow(item)
            print("Write finish")

class FindExtremum:
    '''
    To find the extremum of the list of weibo
    '''
    def __init__(self):
        self.read_path = "D:\\code\\file\\Final_1.csv"
        self.write_path = "D:\\code\\file\\opbFindExtremum.csv"
        self.cprcs = CsvProcesser()
    def find_extremum(self):
        temp = 0
        sum_comment = 0
        line_q = []
        line_list = []
        content_list = self.cprcs.read_csv(self.read_path)
        for line in content_list:
            if len(line_q) < 5:
                line_q.append(line)
            else:
                sum_comment = 0
                temp = int(line_q[0][6])
                for i in range(5):
                    sum_comment += int(line_q[i][6])
                    if int(line_q[i][6]) > temp:
                        temp = int(line_q[i][6])
                line_q.pop(0)
                line_q.append(line)
                if int(line[6]) > (3*sum_comment/5):
                    line_list.append(line)
                    print(line[0])
        self.cprcs.write_csv(line_list, self.write_path)

fe = FindExtremum()
fe.find_extremum()