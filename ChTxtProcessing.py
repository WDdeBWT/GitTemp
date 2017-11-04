# coding:utf-8
# @__Author__ = "WDdeBWT"
# @__Date__ : 2017/10/20

import os
import re
import jieba
import jieba.analyse
import jieba.posseg as pseg
import csv
from textblob import TextBlob


def get_all_kw(read_path, write_path):
    rows = []
    flag = 0
    with open(read_path, 'r') as r:
        for line in r.readlines():
            if re.match(r"EF$", line):
                for row in rows:
                    if row:
                        print(row)
                break
            else:
                if re.match(r"^ID", line):
                    flag = 1
                    line = line[3:]
                    line = line.lower()
                    line = line.strip(';\n')
                    temp_li = line.split("; ")
                    rows += temp_li
                elif re.match(r"^DE", line):
                    flag = 1
                    line = line[3:]
                    line = line.lower()
                    line = line.strip(';\n')
                    temp_li = line.split("; ")
                    rows += temp_li
                elif line[0:3] == "   ":
                    if flag == 1:
                        line = line[3:]
                        line = line.lower()
                        line = line.strip(';\n')
                        temp_li = line.split("; ")
                        rows += temp_li
                    else:
                        pass
                else:
                    flag = 0
    with open(write_path, 'w') as w:
        for row in rows:
            if row:
                w.write(row + "\n")


def get_csv_c(read_path, write_path):
    rows = []
    dict_row = {}
    year = ""
    ti = ""
    ab = ""
    flag = 0
    file_list = os.listdir(read_path)
    for file_name in file_list:
        file_name = os.path.join(read_path, file_name)
        with open(file_name, 'r', encoding="utf-8") as r:
            print(file_name)
            for line in r.readlines():
                print(line)
                if line.startswith("Title-题名:  "):
                    ti = line[11:]
                    continue
                elif line.startswith("Summary-摘要:  "):
                    ab = line[13:]
                    continue
                elif line.startswith("Year-年:  "):
                    year = line[9:]
                    if "《管理科学学报》" not in ti:
                        dict_row = {'YEAR': year, 'TI': ti, 'AB': ab}
                        rows.append(dict_row)
                    year = ""
                    ti = ""
                    ab = ""
                    continue
    write_path = os.path.join(write_path, "chinese_ti_and_ab.csv")
    fieldnames = ["ID", "YEAR", "TI", "AB"]
    stopwords = []
    stopword = (line.strip() for line in open(StopPath, 'r', encoding='UTF-8').readlines())
    for word in stopword:
        stopwords.append(word)
    err_list = ['\ufeff', '\ue56d', '\ue011', '\ue43a']
    stopwords = stopwords + err_list
    csv_li = []
    with open(write_path, 'w', newline="") as w:
        writer = csv.DictWriter(w, fieldnames=fieldnames)
        i = 0
        for di in rows:
            i += 1
            ti = ""
            ti_li = []
            ab = ""
            ab_li = []
            # TI分词
            words = pseg.cut(di["TI"])
            for word, flag in words:
                if flag in ('n', 'ns', 'nt', 'nz', 'an', 'vn', 'un'):
                    if word not in stopwords:
                        ti = ti + " " + word
            # AB分词
            words = pseg.cut(di["AB"])
            for word, flag in words:
                if flag in ('n', 'ns', 'nt', 'nz', 'an', 'vn', 'un'):
                    if word not in stopwords:
                        ab = ab + " " + word
            # 使用textrank提取关键词并提名词的老版本代码
            # nouns = jieba.analyse.textrank(di["AB"], topK=10000, withWeight=False, allowPOS='n')
            # for word in nouns:
            #     if word not in stopwords:
            #         ab = ab + " " + word
            csv_li.append({"ID": i, "YEAR": di["YEAR"], "TI": ti, "AB": ab})
            print(di["YEAR"])
            print(ti)
            print(ab)
            print("--------------------")
        writer.writerows(csv_li)


read_path_e = "F:\\Files\\JAR\\Journal_of_accounting_research.txt"
write_path_e = "F:\\Files\\JAR\\KW_new.txt"

StopPath = "F:\\Files\\stopWordC.txt"

read_path_c = "F:\\Files\\管理科学学报_原始数据\\"
write_path_c = "F:\\Files\\管理科学学报_初步处理\\"

read_path_ch = "K:\\Ori_Chinese\\"
write_path_ch = "K:\\Ori_Chinese_out\\"

# get_all_kw(read_path_e, write_path_e)
get_csv_c(read_path_c, write_path_c)
