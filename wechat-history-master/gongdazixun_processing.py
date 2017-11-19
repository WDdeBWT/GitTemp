# coding:utf-8
# @__Author__ = "WDdeBWT"
# @__Date__ : 2017/10/20

import csv
import os
import re

import jieba
import jieba.analyse
import jieba.posseg as pseg
from textblob import TextBlob


def get_csv_c(read_path, write_path):
    rows = []
    file_list = os.listdir(read_path)
    for file_name in file_list:
        if "text" in file_name:
            file_name = os.path.join(read_path, file_name)
            with open(file_name, 'r', encoding="utf-8") as r:
                print(file_name)
                content_flag = 0
                time_flag = 0
                news_time = ""
                text = []
                for line in r.readlines():
                    #print(line)
                    if (re.search(r'\d{4}-\d{2}-\d{2}', line)) and time_flag == 0:
                        news_time = str(re.search(r'\d{4}-\d{2}-\d{2}', line).group(0))[:7] # 取出时间字符串的前7位（年-月）
                        news_time = news_time[:4] + news_time[5:]
                        news_time = news_time[2:]
                        x = news_time[:2]
                        y = news_time[2:]
                        news_time = str( (int(x)-15)*12 + int(y) + 1950 )
                        time_flag = 1
                    if ("国   际" in line) or ("【国际要闻】" in line):
                        dict_row = {'TIME': news_time, 'TEXT': text}
                        rows.append(dict_row)
                        print(news_time)
                        print("-----contentOVER-----")
                        break
                    if ("HIGHLIGHTS" in line) or ("【国内要闻】" in line) or content_flag == 1:
                        content_flag = 1
                        text.append(line)

    print("----------START----------")
    write_path = os.path.join(write_path, "chinese_ti_and_ab.csv")
    fieldnames = ["ID", "TIME", "TEXT"]
    stopwords = []
    stopword = (line.strip()
                for line in open(StopPath, 'r', encoding='UTF-8').readlines())
    for word in stopword:
        stopwords.append(word)
    err_list = ['\ufeff', '\ue56d', '\ue011', '\ue43a']
    stopwords = stopwords + err_list
    csv_li = []
    with open(write_path, 'w', newline="") as w:
        writer = csv.DictWriter(w, fieldnames=fieldnames)
        i = 0
        for di in rows:
            for text in di["TEXT"]:
                word_list = ""
                # TEXT分词
                words = pseg.cut(text)
                for word, flag in words:
                    if flag in ('n', 'ns', 'nt', 'nz', 'an', 'vn', 'un'):
                        if word not in stopwords:
                            word_list = word_list + " " + word
                if (word_list == " 要闻") or (word_list == ""):
                    continue
                i = i + 1
                csv_li.append({"ID": i, "TIME": di["TIME"], "TEXT": word_list})
                print(di["TIME"])
                print(word_list)
                print("--------------------")
        writer.writerows(csv_li)
    print("----------FINISH----------")


StopPath = "F:\\Files\\stopWordG.txt"

read_path_c = "F:\\Files\\公大资讯历史记录1000_原始数据\\"
write_path_c = "F:\\Files\\公大资讯历史记录1000_初步处理\\"

get_csv_c(read_path_c, write_path_c)
