# coding:utf-8
# @__Author__ = "WDdeBWT"
# @__Date__ : 2017/10/20

import os
import re
import jieba
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
                elif line.startswith("Keyword-关键词:  "):
                    ab = line[14:]
                    continue
                elif line.startswith("Year-年:  "):
                    year = line[9:]
                    dict_row = {'YEAR': year, 'TI': ti, 'AB': ab}
                    rows.append(dict_row)
                    year = ""
                    ti = ""
                    ab = ""
                    continue
    write_path = os.path.join(write_path, "chinese_ti_and_ab.txt")
    with open(write_path, 'w') as w:
        for di in rows:
            w.write(di["YEAR"])
            w.write(di["TI"])
            w.write(di["AB"])


read_path_e = "F:\\Files\\JAR\\Journal_of_accounting_research.txt"
write_path_e = "F:\\Files\\JAR\\KW_new.txt"

read_path_c = "F:\\Files\\管理科学学报_原始数据\\"
write_path_c = "F:\\Files\\管理科学学报_初步处理\\"

# get_all_kw(read_path_e, write_path_e)
get_csv_c(read_path_c, write_path_c)




















