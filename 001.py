# encoding=utf-8
import jieba
import jieba.analyse

ReadPath = "D:\\2016ab.txt"
wordList = []
lines = ""
with open(ReadPath, 'r') as r:
	for line in r.readlines():
		lines += line
	tf = jieba.analyse.extract_tags(lines, topK = 30, withWeight = True)
	for t in tf:
		print(t)
