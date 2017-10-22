# _*_ coding:utf-8 _*_
__author__ = "WDdeBWT"
__date__ = "2017/10/22 3:15"

import csv
import os

fieldnames = ["NAME", "MAX", "LINE"]
filename = "D:\\1\\guanxiaotong"
for i in range(1):
    file_name = filename + str(i+1) + ".csv"
    new_name = filename + str(i+1) + "new.csv"
    with open(file_name, 'r') as csv_r:
        reader = csv.reader(csv_r)
        with open(new_name, 'wb') as csv_w:
            writer = csv.DictWriter(csv_w, fieldnames=fieldnames)
            newli = []
            rows = [row for row in reader]
            name = rows[0][0]
            time = rows[0][1]
            flag = 0
            flagli = []
            line = ""
            for row in rows:
                if row[0] == name:
                    name = row[0]
                    line += row[5]
                    if row[1] == time:
                        flag += 1
                    else:
                        flagli.append(flag)
                        time = row[1]
                        flag = 1
                else:
                    flagli.append(flag)
                    flagli.sort(reverse=True)
                    flag = flagli[0]
                    newli.append({"NAME": name, "MAX": flag, "LINE": line})
                    flagli = []
                    name = row[0]
                    line = row[5]
                    time = row[1]
                    flag = 1
                    flagli.append(flag)
            flagli.sort(reverse=True)
            flag = flagli[0]
            newli.append({"NAME": name, "MAX": flag, "LINE": line})
            writer.writerows(newli)
            print(newli)

