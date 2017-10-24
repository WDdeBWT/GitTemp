# coding: utf-8
# @__Author__ = "WDdeBWT"
# @__Date__ : 2017/10/20

import os
import re
import csv
from textblob import TextBlob


def read_and_write(read__path, write__path):
    fieldnames = ["ID", "YEAR", "TI", "AB"]
    rows = []
    year = ""
    ti = ""
    ab = ""
    i = 0
    with open(read__path, 'r') as r:
        with open(write__path, "w", newline="") as datacsv:
            writer = csv.DictWriter(datacsv, fieldnames=fieldnames)
            for line in r.readlines():
                if re.match(r"EF$", line):
                    writer.writerows(rows)
                    print(rows)
                    break
                else:
                    if re.match(r"^AB", line):
                        ab = line[3:]
                        blob = TextBlob(ab)
                        ab = blob.noun_phrases
                    if re.match(r"^TI", line):
                        ti = line[3:]
                        blob = TextBlob(ti)
                        ti = blob.noun_phrases
                    elif re.match(r"^PY", line):
                        i = i + 1
                        year = line[3:]
                        rows.append({"ID": i, "YEAR": year, "TI": ti, "AB": ab})
                        year = ""
                        ti = ""
                        ab = ""


read_path = "F:\\Files\\JAR\\Journal_of_accounting_research.txt"
write_path = "F:\\Files\\JAR\\XXX.csv"
read_and_write(read_path, write_path)
