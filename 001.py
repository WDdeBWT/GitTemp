# coding=utf-8

import sys
import io
import jieba
import jieba.analyse
import os

text = []
StopPath = "D:\\StopWord.txt"
errlist = ('\ufeff', '\ue56d')
with open("D:\\test1.txt", 'w') as f:
	for x in range(5):
		Path = os.path.join("D:\\", (str)(2017-x))
		Path = os.path.join(Path, (str)(2017-x) + "ab.txt")
		with open(Path, "r", encoding='UTF-8') as r:
			for line in r.readlines():
				tag = jieba.cut(line)
				for wd in tag:
					text.append(wd)
	for word in text:
		stopwords = (line.strip() for line in open(StopPath,'r',encoding='UTF-8').readlines())
		if word not in stopwords:
			if word not in errlist:
				f.write(word + ' ')
				print(word)
