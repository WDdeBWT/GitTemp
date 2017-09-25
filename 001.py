# encoding=utf-8
import jieba

ReadPath = "D:\\2016ab.txt"
wordList = []
with open(ReadPath, 'r') as r:
	for line in r.readlines():
		words = jieba.cut(line)
		for word in words:
			wordList.append(word)
		#print("Default Mode: " + "/ ".join(words))  # 精确模式
	print("Default Mode: " + "/ ".join(wordList))
